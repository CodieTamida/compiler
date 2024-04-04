import os
from common.enums import TokenType
from components.lexcical_analyzer import Lexer, Token
from components.syntax_analyzer import Parser

def write_to_file(filename, content):
    """
    Writes the given content to a file with the specified filename.

    Parameters:
    - filename (str): The name of the file to write to.
    - content (str): The content to be written to the file.
    """
    file = open(filename, 'w')
    file.write(content)
    file.close()

def get_result_from_parser(filename):
    """
    Parses a file using a lexer and parser, returning the result.

    Parameters:
    - filename (str): The name of the file to parse.

    Returns:
    - result: The parsed result obtained from the parser.
    """
    # Lexer: Load from file
    lexer = Lexer(filename)

    # Parser: Call parse() method
    parser = Parser(lexer, debug_print=True)
    print("\n")
    result = parser.parse()
    
    return result