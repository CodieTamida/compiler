import argparse
from functions import *
from components.lexcical_analyzer import Lexer


def main(input_file, output_file):
    """
    Process the input file, tokenize its contents using a Lexer instance, 
    and write the tokenized output to the specified output file.

    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.

    Returns:
        None
    """

    # Open a file for writing
    with open(output_file, 'w') as file:
        # Write table headers
        file.write(f"{'token':<20} {'lexeme':<10}\n")
        file.write(f'{"-" * 31}\n')

        # Create a Lexer instance
        lexer = Lexer(input_file)

        # Loop through each token in the file
        while lexer.has_token():
            # Get token
            token = lexer.next_token()

            # Write to file & Print to console
            text = f"{token.token_type.name.lower():<20} {token.lexeme}\n"
            file.write(text)
            print(text, end='')


if __name__ == '__main__':
    # Parses command-line arguments using argparse
    # to process input and output file paths, and then calls the main function.
    parser = argparse.ArgumentParser(description='Compile a source file')
    parser.add_argument('input_file', type=str, help='Input file path')
    parser.add_argument('output_file', type=str, help='Output file path')
    args = parser.parse_args()

    main(args.input_file, args.output_file)
