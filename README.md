Playbac was my project for [Cornhacks 2020](https://cornhacks.com/). For more information about my project or the other projects at Cornhacks 2020, see the [Devpost page](https://devpost.com/software/playbric)!

## What is it? 
Playbac is a Chrome extension that scrapes any content-based website (blog, news article, etc) for "meaningful" text. Then, based on a language and gender selection, it will generate an audio transcription of the text and will allow you to play that audio right from your browser.

## Inspiration
There were a few sources of inspiration for this project:

- Much of the internet is in English, which can sometimes be an accessibility issue. I wanted to work on this project as a way to help more people access information and content that they might not be able to otherwise.
- On another accessibility note, some people have trouble reading screens. This could help them by providing audio information.

## How I built it
I wrote a Chrome extension that provides a UI via Google Chrome. The Chrome extension then and submits the data to an AWS Lambda function that extracts "meaningful text" from the website data of the specified URL. Then, the Lambda function calls AWS Polly to transcribe that text to audio. AWS Polly then stores the audio output in an S3 bucket. The Chrome extension asynchronously waits for the AWS Lambda and Polly jobs to finish so that it can grab the audio file stored in S3 so that the user can listen to the audio.

## What's next for Playbac
- Incorporate AWS Translate to translate between different languages before providing a transcription
- Save link between website URLs and transcription audio files in a database to prevent duplicate transcription
- Allow people to register/login with OAUTH and save their account info.
