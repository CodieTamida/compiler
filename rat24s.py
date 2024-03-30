import argparse
from components.lexcical_analyzer import Lexer
from components.syntax_analyzer import Parser


def extract_tokens(args):
    # Create a Lexer instance
    lexer = Lexer(args.input)

    if args.output:
        # Open a file for writing
        with open(args.output, 'w') as file:
            # Write table headers
            file.write(f"{'token':<20} {'lexeme':<10}\n")
            file.write(f'{"-" * 31}\n')

            for token in lexer.tokens:
                text = f"{token.token_type.name.lower():<20} {token.lexeme}\n"
                file.write(text)
                if args.verbose:
                    print(text, end="")
    # Verbose mode
    elif args.verbose:
        for token in lexer.tokens:
            text = f"{token.token_type.name.lower():<20} {token.lexeme}\n"
            print(text, end="")


def check_syntax(args):
    # Create a Lexer instance
    lexer = Lexer(args.input)

    parser = Parser(lexer, debug_print=args.verbose)
    parsing_success = parser.parse()

    if args.output:
        # Open a file for writing
        with open(args.output, 'w') as file:
            for text in parser.get_logs():
                file.write(text)
                file.write('\n')

    # Display parsing result
    print('-' * 50)
    print(f"Filename: {args.input}")
    print(f"Number of Tokens: {len(lexer.tokens)}")
    if parsing_success:
        print("\033[32m", "Syntax is correct", "\033[0m", sep='')
    else:
        print("\033[31m", "Error: Syntax is incorrect", "\033[0m", sep='')

    print('-' * 50)


def main(args):
    """
    Process the input file, tokenize its contents using a Lexer instance, 
    and write the tokenized output to the specified output file.

    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.

    Returns:
        None
    """
    # Token-only mode
    if args.tokens:
        extract_tokens(args)
    # Check syntax mode
    elif args.syntax:
        check_syntax(args)


if __name__ == '__main__':
    # Parses command-line arguments using argparse
    # to process input and output file paths, and then calls the main function.
    parser = argparse.ArgumentParser(description='Compile a source file')
    parser.add_argument("input", type=str, help="Input file path")
    parser.add_argument("-o", '--output', type=str, help="Output file path")
    parser.add_argument("-t", "--tokens", action="store_true",
                        help="Extract tokens only, but don't do anything beyond that.")
    parser.add_argument("-s", "--syntax", action="store_true",
                        help="Check the code for syntax errors, but don't do anything beyond that.")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Enable verbose mode")

    args = parser.parse_args()

    main(args)
