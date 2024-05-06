import os
from common.enums import TokenType
from components.lexcical_analyzer import Lexer, Token
from components.syntax_analyzer import Parser
from components.code_generator import CodeGenerator


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


def get_result_from_code_generator(filename):
    """
    Generates assembly code from a given filename.

    Parameters:
    - filename (str): The name of the file to generate assembly code from.

    Returns:
    - str: The assembly code generated from the input file.
    """
    asm_code = str()

    # CodeGenerator
    try:
        # Lexer: Load from file
        lexer = Lexer(filename)

        # CodeGenerator
        codegen = CodeGenerator(lexer, initial_memory_address=5000)
        asm_code = codegen.generate_assembly_code()

        # Print tables
        print("\n")
        codegen.print_symbol_table()
        print()
        codegen.print_instruction_table()
    except Exception as err:
        codegen.print_symbol_table()
        print()
        print("\033[91m", end="")  # Print ANSI escape code for red color
        print(f"{type(err).__name__}: {err}\nParsing failed")
        print("\033[0m", end="")  # Print ANSI escape code to reset
    finally:
        return asm_code
