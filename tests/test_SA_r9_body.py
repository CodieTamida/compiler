import unittest
import os
from common.enums import TokenType
from components.lexcical_analyzer import Lexer, Token
from components.syntax_analyzer import Parser

class BodyTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self) -> None:
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self) -> None:
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_body(self):
        input_string = "$ $ $ { a + b } $"

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        lexer = Lexer(self.SAMPLE_FILE_PATH)

        parser = Parser(lexer, debug_print=True)
        parser.debug_print()
        parser.debug_print()
        parsing_success = parser.parse()

        self.assertTrue(parsing_success)

    def test_body_no_closing_brace(self):
        input_string = "$$ { a- 2 $"
        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)
        
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        parser = Parser(lexer, debug_print=True)
        parser.debug_print()
        parser.debug_print()
        parsing_success = parser.parse()

        self.assertFalse(parsing_success)

    def test_body_no_opening_brace(self):
        input_string = "$ a - -5}$"
        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        lexer = Lexer(self.SAMPLE_FILE_PATH)
        parser = Parser(lexer, debug_print=True)
        parser.debug_print()
        parser.debug_print()
        parsing_success = parser.parse()

        self.assertFalse(parsing_success)
        




if __name__ == '__main__':
    unittest.main()
    
