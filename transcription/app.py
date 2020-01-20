import json
import logging
import os
import random
import re
from urllib.parse import urlparse

# 3rd party packages
import boto3
from goose3 import Goose
from validators import url, ValidationFailure

# project imports
from constants import language_to_voice_map, OUTPUT_BUCKET_NAME, POLLY_ENGINE, ENGLISH_CODE
from exception import LanguageMappingException
from gender import Gender


s3_client = boto3.client('s3', region_name='us-east-2')
polly_client = boto3.client('polly', region_name='us-east-2')
translate_client = boto3.client('translate', region_name='us-east-2')

def clean_lambda_params(data):
    expected_params = ["url", "language", "region", "gender"]
    cleaned_params = dict()
    for k, v in data.items():
        # ignore any unexpected input params
        if k in expected_params:
            cleaned_params[k] = v
    if "region" not in data:
        cleaned_params["region"] = None
    return cleaned_params

def get_language_voice_mapping(language, region=None, gender=Gender.FEMALE):
    if region is not None:
        language = "{0}:{1}".format(region, language)
    try:
        language_obj = language_to_voice_map[language]
        voice = random.choice(language_obj[gender])
        return voice, language_obj["code"], language_obj["translate_code"] # TODO: figure out this mapping from the map obj above
    except Exception as e:
        message = str(e) + "\n\n[EXCEPTION]: No language associated with the following parameters:\nLanguage: {},\nRegion: {},\nGender: {}".format(language, region, gender)
        raise LanguageMappingException(message)

def process_event(data):
    fnc_params = clean_lambda_params(data)
    target_url = fnc_params["url"] # TODO: add url param to request object from javascript
    try:
        url(target_url)
    except ValidationFailure as validationFailure: 
        raise Exception("[EXCEPTION]: Invalid URL\n\nValidationFailure ==> {}".format(str(validationFailure)))
    voice_id, lang_code, translate_code = get_language_voice_mapping(fnc_params["language"], fnc_params["region"], fnc_params["gender"])
    print("[REQUEST DETAILS] url: {0}, voiceId: {1}, languageCode: {2}".format(target_url, voice_id, lang_code))

    text_to_transcribe = Goose().extract(url=target_url).cleaned_text
    if translate_code != ENGLISH_CODE:
        # translate
        response = translate_client.translate_text(Text=text_to_transcribe, 
            SourceLanguageCode=ENGLISH_CODE, TargetLanguageCode=translate_code)
        text_to_transcribe = response["TranslatedText"]

    # submit the contents to amazon polly for synthesis task: https://docs.aws.amazon.com/polly/latest/dg/API_StartSpeechSynthesisTask.html
    response = polly_client.start_speech_synthesis_task(
        Engine=POLLY_ENGINE,
        OutputFormat='mp3', # Audio output
        TextType='text',
        Text=text_to_transcribe, # main content from the webpage
        VoiceId=voice_id,
        LanguageCode=lang_code,
        OutputS3BucketName=OUTPUT_BUCKET_NAME, # TODO: Amazon S3 bucket name to which the output file will be saved.
    )

    return 200, {
        "outputUri": response["SynthesisTask"]["OutputUri"],
        "taskId": response["SynthesisTask"]["TaskId"]
    }

def lambda_handler(event, context):
    """
    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format. AWS Lambda uses this parameter to pass in data to the handler.
        This parameter is usually of the Python dict type. It can also be list, str, int, float, or NoneType type.
        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes. AWS Lambda uses this parameter to provide runtime information to your
        handler. This parameter is of the LambdaContext type.

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict
        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    statusCode = 500
    response = None
    try:
        statusCode, response = process_event(event)
    except LanguageMappingException as lme:
        response = lme.message
    except Exception as e:
        response = str(e)
    return {
        "statusCode": statusCode,
        "response": response
    }
