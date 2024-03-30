from enum import Enum, auto

class SyntaxType(Enum):
    NUMBER = auto()

    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    BRACKETS = auto()


    OPEN_BRACKET = auto()
    CLOSE_BRACKET = auto()

    DOT = auto()

    WHITE_SPACE = auto()
    EOF = auto()

    BAD_TOKEN = auto()