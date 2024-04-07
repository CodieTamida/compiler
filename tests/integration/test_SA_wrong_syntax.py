import unittest
import os
from components.lexcical_analyzer import Lexer, Token
from tests.integration.helpers import write_to_file, print_file, read_tokens_from_lexer_output, read_tokens_from_parser_output, run_command


class WrongSyntaxTestCase(unittest.TestCase):
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

    def test_endif_is_missing(self):
        # Arrange
        input_string = """
            $
                function alert(message integer) 
                {
                    if (len(message) > 0)
                    {
                        print(message);
                    }
                    
                }
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
        try:
            self.assertNotEquals(tokens_from_lexer, tokens_from_parser)
        except:
            print_file(self.PARSER_OUTPUT_PATH)
            raise AssertionError("Expected the input to have a Syntax Error, but found Syntax is Correct")
        self.assertIn("Syntax is incorrect", check_syntax_command_output)
