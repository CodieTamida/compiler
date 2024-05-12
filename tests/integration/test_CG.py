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
            [* this is comment for this sample code for assignment 3 *]
            $
            [* NO function definitions *]
            $
                integer i, max, sum; [* declarations *]
            $
                sum = 0;
                i = 1;
                scan (max);
                while (i < max) {
                    sum = sum + i;
                    i = i + 1;
                }
                endwhile
                print (sum + max);
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 0\n")
        string_builder.write("POPM 5002\n")
        string_builder.write("PUSHI 1\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("SIN\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("LABEL\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("LES\n")
        string_builder.write("JUMP0 21\n")
        string_builder.write("PUSHM 5002\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("A\n")
        string_builder.write("POPM 5002\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHI 1\n")
        string_builder.write("A\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("JUMP 7\n")
        string_builder.write("PUSHM 5002\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("A\n")
        string_builder.write("SOUT\n")

        string_builder.write("\n")
        string_builder.write("\n")
        string_builder.write("Symbol Table:\n")
        string_builder.write("Identifier     Address   Type           \n")
        string_builder.write("----------------------------------------\n")
        string_builder.write("i              5000      INTEGER        \n")
        string_builder.write("max            5001      INTEGER        \n")
        string_builder.write("sum            5002      INTEGER        \n")

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
