
class ValidationException(Exception):
    pass

class InvalidNumberOfArgumentsException(ValidationException):
    def __init__(self, str):
        self.str = str

    def __str__(self):
        return f"InvalidNumberOfArgumentsException: {self.str}"


class IllegalCharacterException(ValidationException):
    def __init__(self, str):
        self.str = str

    def __str__(self):
        return f"IllegalCharacterException: {self.str}"

class ValueOutOfBoundsException(ValidationException):
    def __init__(self, bounds, val):
        self.bounds = bounds
        self.val = val

    def __str__(self):
        return f"ValueOutOfBoundsException: Expected:{self.bounds} Got:{self.val}"
