OUTPUT_BUCKET_NAME = "transcription-output-bucket-cornhacks"

POLLY_ENGINE = "standard"

language_to_voice_map = {
    "arabic": {
        "female": ["Zeina"],
        "code": "arb"
    },
    "chinese": {
        "female": ["Zhiyu"],
        "code": "cmn-CN"
    },
    "danish": {
        "female": ["Naja"],
        "male": ["Mads"],
        "code": "da-DK"
    },
    "dutch": {
        "female": ["Lotte"],
        "male": ["Ruben"],
        "code": "nl-NL"
    },
    "australian:english": {
        "female": ["Nicole"],
        "male": ["Russell"],
        "code": "en-AU"
    },
    "british:english": {
        "female": ["Amy", "Emma"],
        "male": ["Brian"],
        "code": "en-GB"
    },
    "indian:english": {
        "female": ["Aditi", "Raveena"],
        "code": "en-IN"
    },
    "us:english": {
        "female": ["Ivy", "Joanna", "Kendra", "Kimberly", "Salli"],
        "male": ["Joey", "Justin", "Matthew"],
        "code": "en-US"
    },
    "welsh:english": {
        "male": ["Geraint"],
        "code": "en-GB-WLS"
    },
    "french": {
        "female": ["Céline", "Léa"],
        "male": ["Mathieu"],
        "code": "fr-FR"
    },
    "canadian:french": {
        "female": ["Chantal"],
        "code": "fr-CA"
    },
    "german": {
        "female": ["Marlene", "Vicki"],
        "male": ["Hans"],
        "code": "de-DE"
    },
    "hindi": {
        "female": ["Aditi"],
        "code": "hi-IN"
    },
    "icelandic": {
        "female": ["Dóra"],
        "male": ["Karl"],
        "code": "is-IS"
    },
    "italian": {
        "female": ["Carla", "Bianca"],
        "male": ["Giorgio"],
        "code": "it-IT"
    },
    "japanese": {
        "female": ["Mizuki"],
        "male": ["Takumi"],
        "code": "ja-JP"
    },
    "korean": {
        "female": ["Seoyeon"],
        "code": "ko-KR"
    },
    "norwegian": {
        "female": ["Liv"],
        "code": "nb-NO"
    },
    "polish": {
        "female": ["Ewa", "Maja"],
        "male": ["Jacek", "Jan"],
        "code": "pl-PL"
    },
    "brazilian:portuguese": {
        "female": ["Vitória"],
        "male": ["Ricardo"],
        "code": "pt-BR"
    },
    "european:portuguese": {
        "female": ["Inês"],
        "male": ["Cristiano"],
        "code": "pt-PT"
    },
    "romanian": {
        "female": ["Carmen"],
        "code": "ro-RO"
    },
    "russian": {
        "female": ["Tatyana"],
        "male": ["Maxim"],
        "code": "ru-RU"
    },
    "european:spanish": {
        "female": ["Conchita", "Lucia"],
        "male": ["Enrique"],
        "code": "es-ES"
    },
    "mexican:spanish": {
        "female": ["Mia"],
        "code": "es-MX"
    },
    "us:spanish": {
        "female": ["Penélope"],
        "male": ["Miguel"],
        "code": "es-US"
    },
    "swedish": {
        "female": ["Astrid"],
        "code": "sv-SE"
    },
    "turkish": {
        "female": ["Filiz"],
        "code": "tr-TR"
    },
    "welsh": {
        "female": ["Gwyneth"],
        "code": "cy-GB"
    },
}