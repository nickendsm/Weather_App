from error_msges import FAIL_TO_PARSE_MSG, UNKNOWN_COMMAND_MSG, FILE_NOT_FOUND_MSG, FAILED_TO_OPEN_MSG
from error_msges import ERRORS_HTTP, UNKNOWN_ERROR


class BadArgs(Exception):
    message: str = FAIL_TO_PARSE_MSG


class UnknownCommand(Exception):
    message: str = UNKNOWN_COMMAND_MSG


class FileNotFound(Exception):
    message: str = FILE_NOT_FOUND_MSG


class FailedToOpenFile(Exception):
    message: str = FAILED_TO_OPEN_MSG


class HTTPError(Exception):
    def __init__(self, code):
        self.message = ERRORS_HTTP.get(code, UNKNOWN_ERROR)
