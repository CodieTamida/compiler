import unittest
import os
from components.lexcical_analyzer import Lexer, Token
from tests.integration.helpers import write_to_file, read_tokens_from_lexer_output, read_tokens_from_parser_output, run_command


class SyntaxAnalyzerTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"
    LEXER_OUTPUT_PATH = "tests/lexer_output.txt"
    PARSER_OUTPUT_PATH = "tests/parser_output.txt"

    def clean_up(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

        if os.path.exists(self.LEXER_OUTPUT_PATH):
            os.remove(self.LEXER_OUTPUT_PATH)
        
        if os.path.exists(self.PARSER_OUTPUT_PATH):
            os.remove(self.PARSER_OUTPUT_PATH)

    def setUp(self) -> None:
        self.clean_up()

    def tearDown(self) -> None:
        self.clean_up()

    def test_small(self):
        # Arrange
        input_string = """
            $

            $

            $ 
                [*This is a comment*]
                [* This is anther comment *]
                a= b + z;
            $
            """

        # Act 1: Create a test file
        write_to_file(self.SAMPLE_FILE_PATH, input_string)

        # Act 2 Run rat24s.py
        extract_tokens_command = f"python3 rat24s.py {self.SAMPLE_FILE_PATH} --tokens --output {self.LEXER_OUTPUT_PATH}"
        check_syntax_command = f"python3 rat24s.py {self.SAMPLE_FILE_PATH} --syntax --output {self.PARSER_OUTPUT_PATH}"

        run_command(extract_tokens_command)
        check_syntax_command_output = run_command(check_syntax_command)

        tokens_from_lexer = read_tokens_from_lexer_output(self.LEXER_OUTPUT_PATH)
        tokens_from_parser = read_tokens_from_parser_output(self.PARSER_OUTPUT_PATH)

        # Assert
        self.assertListEqual(tokens_from_lexer, tokens_from_parser)
        self.assertIn("Syntax is correct", check_syntax_command_output)

    def test_medium(self):
        # Arrange
        input_string = """
            $
                function alert(p1, p2 real, x, y, z boolean) 
                {
                    sum = p1 + p2;
                }
            $
            
            $ 
                { a= b + z; } 
                while (d == true)
                {
                    a= b + z;
                    if (a > 0)
                        a = a / 2;
                    endif
                }
                endwhile
            $
            """

        # Act 1: Create a test file
        write_to_file(self.SAMPLE_FILE_PATH, input_string)

        # Act 2 Run rat24s.py
        extract_tokens_command = f"python3 rat24s.py {self.SAMPLE_FILE_PATH} --tokens --output {self.LEXER_OUTPUT_PATH}"
        check_syntax_command = f"python3 rat24s.py {self.SAMPLE_FILE_PATH} --syntax --output {self.PARSER_OUTPUT_PATH}"

        run_command(extract_tokens_command)
        check_syntax_command_output = run_command(check_syntax_command)

        tokens_from_lexer = read_tokens_from_lexer_output(self.LEXER_OUTPUT_PATH)
        tokens_from_parser = read_tokens_from_parser_output(self.PARSER_OUTPUT_PATH)

        # Assert
        self.assertListEqual(tokens_from_lexer, tokens_from_parser)
        self.assertIn("Syntax is correct", check_syntax_command_output)


if __name__ == '__main__':
    unittest.main()