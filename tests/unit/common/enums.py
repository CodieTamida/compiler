from enum import Enum


class TokenType(Enum):
    IDENTIFIER = 1
    KEYWORD = 2
    REAL = 3
    INTEGER = 4
    OPERATOR = 5
    SEPARATOR = 6
    UNKNOWN = 7
