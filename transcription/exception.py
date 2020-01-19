class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class LanguageMappingException(Error):
    """Exception raised for language mapping exception.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message