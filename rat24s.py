import argparse
from components.lexcical_analyzer import Lexer
from components.syntax_analyzer import Parser


def print_tokens(lexer: Lexer):
    for token in lexer.tokens:
        text = f"{token.token_type.name.lower():<20} {token.lexeme}"
        print(text)


def write_tokens_to_file(lexer: Lexer, output_file: str):
    with open(output_file, 'w') as file:
        # Write table headers
        file.write(f"{'token':<20} {'lexeme':<10}\n")
        file.write(f'{"-" * 31}\n')

        # Write tokens
        for token in lexer.tokens:
            text = f"{token.token_type.name.lower():<20} {token.lexeme}\n"
            file.write(text)


def lexical_analyze(input_file, output_file, verbose):
    lexer = Lexer(input_file)

    if verbose:
        print_tokens(lexer)

    if output_file:
        write_tokens_to_file(lexer, output_file)

    return lexer


def syntax_analyze(input_file, output_file, verbose):
    lexer = lexical_analyze(input_file, output_file, False)

    parser = Parser(lexer, debug_print=False)
    parsing_success = parser.parse()

    if verbose:
        for text in parser.get_logs():
            print(text)

    if output_file:
        # Open a file for writing
        with open(output_file, 'w') as file:
            for text in parser.get_logs():
                file.write(text)
                file.write('\n')

    # Print parsing result to console
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
        lexical_analyze(args.input, args.output, args.verbose)
    # Check syntax mode
    else:
        syntax_analyze(args.input, args.output, args.verbose)


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
