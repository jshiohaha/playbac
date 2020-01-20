OUTPUT_BUCKET_NAME = "transcription-output-bucket-cornhacks"

POLLY_ENGINE = "standard"
ENGLISH_CODE = "en"

language_to_voice_map = {
    "arabic": {
        "female": ["Zeina"],
        "code": "arb",
        "translate_code": "ar"
    },
    "chinese": {
        "female": ["Zhiyu"],
        "code": "cmn-CN",
        "translate_code": "zh"
    },
    "danish": {
        "female": ["Naja"],
        "male": ["Mads"],
        "code": "da-DK",
        "translate_code": "da"
    },
    "dutch": {
        "female": ["Lotte"],
        "male": ["Ruben"],
        "code": "nl-NL",
        "translate_code": "nl"
    },
    "australian:english": {
        "female": ["Nicole"],
        "male": ["Russell"],
        "code": "en-AU",
        "translate_code": "en"
    },
    "british:english": {
        "female": ["Amy", "Emma"],
        "male": ["Brian"],
        "code": "en-GB",
        "translate_code": "en"
    },
    "indian:english": {
        "female": ["Aditi", "Raveena"],
        "code": "en-IN",
        "translate_code": "en"
    },
    "us:english": {
        "female": ["Ivy", "Joanna", "Kendra", "Kimberly", "Salli"],
        "male": ["Joey", "Justin", "Matthew"],
        "code": "en-US",
        "translate_code": "en"
    },
    "welsh:english": {
        "male": ["Geraint"],
        "code": "en-GB-WLS",
        "translate_code": "en"
    },
    "french": {
        "female": ["Céline", "Léa"],
        "male": ["Mathieu"],
        "code": "fr-FR",
        "translate_code": "fr"
    },
    "canadian:french": {
        "female": ["Chantal"],
        "code": "fr-CA",
        "translate_code": "fr-CA"
    },
    "german": {
        "female": ["Marlene", "Vicki"],
        "male": ["Hans"],
        "code": "de-DE",
        "translate_code": "de"
    },
    "hindi": {
        "female": ["Aditi"],
        "code": "hi-IN",
        "translate_code": "hi"
    },
    # "icelandic": {
    #     "female": ["Dóra"],
    #     "male": ["Karl"],
    #     "code": "is-IS"
    # },
    "italian": {
        "female": ["Carla", "Bianca"],
        "male": ["Giorgio"],
        "code": "it-IT",
        "translate_code": "it"
    },
    "japanese": {
        "female": ["Mizuki"],
        "male": ["Takumi"],
        "code": "ja-JP",
        "translate_code": "ja"
    },
    "korean": {
        "female": ["Seoyeon"],
        "code": "ko-KR",
        "translate_code": "ko"
    },
    "norwegian": {
        "female": ["Liv"],
        "code": "nb-NO",
        "translate_code": "no"
    },
    "polish": {
        "female": ["Ewa", "Maja"],
        "male": ["Jacek", "Jan"],
        "code": "pl-PL",
        "translate_code": "pl"
    },
    "brazilian:portuguese": {
        "female": ["Vitória"],
        "male": ["Ricardo"],
        "code": "pt-BR",
        "translate_code": "pt"
    },
    "european:portuguese": {
        "female": ["Inês"],
        "male": ["Cristiano"],
        "code": "pt-PT",
        "translate_code": "pt"
    },
    "romanian": {
        "female": ["Carmen"],
        "code": "ro-RO",
        "translate_code": "ro"
    },
    "russian": {
        "female": ["Tatyana"],
        "male": ["Maxim"],
        "code": "ru-RU",
        "translate_code": "ru"
    },
    "european:spanish": {
        "female": ["Conchita", "Lucia"],
        "male": ["Enrique"],
        "code": "es-ES",
        "translate_code": "es"
    },
    "mexican:spanish": {
        "female": ["Mia"],
        "code": "es-MX",
        "translate_code": "es"
    },
    "us:spanish": {
        "female": ["Penélope"],
        "male": ["Miguel"],
        "code": "es-US",
        "translate_code": "es"
    },
    "swedish": {
        "female": ["Astrid"],
        "code": "sv-SE",
        "translate_code": "sv"
    },
    "turkish": {
        "female": ["Filiz"],
        "code": "tr-TR",
        "translate_code": "tr"
    },
    # "welsh": {
    #     "female": ["Gwyneth"],
    #     "code": "cy-GB"
    # },
}