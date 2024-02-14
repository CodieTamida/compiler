from common.enums import TokenType
from io import StringIO


def tokenize(input_str) -> tuple:
    """
    Tokenizes a given input string into a sequence of tokens, represented as tuples of (TokenType, value).

    Parameters:
    input_str (str): The input string to be tokenized.

    Returns:
    tuple: A tuple containing tokens represented as tuples of (TokenType, value).
    """

    ###########################################
    # THIS FUNCTION NEEDS TO BE REIMPLEMENTED #
    ###########################################
    tokens = [
        (TokenType.KEYWORD, "while"),
        (TokenType.SEPARATOR, "("),
        (TokenType.IDENTIFIER, "fahr"),
        (TokenType.OPERATOR, "<="),
        (TokenType.IDENTIFIER, "upper"),
        (TokenType.SEPARATOR, ")"),
        (TokenType.SEPARATOR, "{"),
        (TokenType.IDENTIFIER, "a"),
        (TokenType.OPERATOR, "="),
        (TokenType.REAL, "23.00"),
        (TokenType.SEPARATOR, ";"),
        (TokenType.IDENTIFIER, "b"),
        (TokenType.OPERATOR, "="),
        (TokenType.REAL, "9"),
        (TokenType.SEPARATOR, ";"),
        (TokenType.SEPARATOR, "}"),
    ]

    return tuple(tokens)
