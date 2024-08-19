class ArgumentError(Exception):
    def __init__(self, message="Incorrect number of arguments passed"):
        super().__init__(message)


class ApplicationError(Exception):
    def __init__(self, message="Application error"):
        super().__init__(message)


class DirectoryError(Exception):
    def __init__(self, message="Invalid or non-existent directory"):
        super().__init__(message)


class FileError(Exception):
    def __init__(self, message="Invalid or non-existent file"):
        super().__init__(message)


class FlagError(Exception):
    def __init__(self, message="Incorrect flags passed"):
        super().__init__(message)


class RedirectError(Exception):
    def __init__(self, message="Incorrect redirection"):
        super().__init__(message)
