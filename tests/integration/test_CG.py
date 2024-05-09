import unittest
import os
from io import StringIO
from components.lexcical_analyzer import Lexer, Token
from tests.integration.helpers import write_to_file, print_file, read_tokens_from_lexer_output, read_tokens_from_parser_output, run_command


class CodeGeneratorTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"
    LEXER_OUTPUT_PATH = "tests/lexer_output.txt"
    PARSER_OUTPUT_PATH = "tests/parser_output.txt"
    CODEGEN_OUTPUT_PATH = "tests/codegen_output.txt"

    def clean_up(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

        if os.path.exists(self.LEXER_OUTPUT_PATH):
            os.remove(self.LEXER_OUTPUT_PATH)

        if os.path.exists(self.PARSER_OUTPUT_PATH):
            os.remove(self.PARSER_OUTPUT_PATH)

        if os.path.exists(self.CODEGEN_OUTPUT_PATH):
            os.remove(self.CODEGEN_OUTPUT_PATH)

    def setUp(self) -> None:
        self.clean_up()

    def tearDown(self) -> None:
        self.clean_up()

    def test_small(self):
        # Arrange
        input_string = """
            $
            $
                integer a, b, c;
            $
                a = 128;
                b = -256;
                c = 512;
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 128\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("PUSHI -256\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHI 512\n")
        string_builder.write("POPM 5002\n")
        expected_output = string_builder.getvalue()

        # Act 1: Create a source file
        write_to_file(self.SAMPLE_FILE_PATH, input_string)

        # Act 2: Run rat24s.py to compile the source file and generate the target file
        command = f"python3 rat24s.py {self.SAMPLE_FILE_PATH} --assembly --output {self.CODEGEN_OUTPUT_PATH}"
        command_output = run_command(command)
        
        # Act 3: Load the target file
        actual_output = None
        with open(self.CODEGEN_OUTPUT_PATH, 'r') as file:
            actual_output = file.read()

        # Assert
        self.assertIn("successful", command_output)
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
