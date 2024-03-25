import unittest
import os
from common.enums import TokenType
from components.lexcical_analyzer import Lexer, Token
from components.syntax_analyzer import Parser


class R1_Rat24STestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    @unittest.skip
    def test_opt_function_definition(self):
        # Arrange
        input_string = "$ function f1() $ $ a = b; $"
        expected_tokens = [
            Token("$", TokenType.SEPARATOR),
            Token("function", TokenType.KEYWORD),
            Token("f1", TokenType.IDENTIFIER),
            Token("(", TokenType.SEPARATOR),
            Token(")", TokenType.SEPARATOR),
            Token("$", TokenType.SEPARATOR),
            Token("$", TokenType.SEPARATOR),
            Token("a", TokenType.IDENTIFIER),
            Token("=", TokenType.OPERATOR),
            Token("b", TokenType.IDENTIFIER),
            Token(";", TokenType.SEPARATOR),
            Token("$", TokenType.SEPARATOR)
        ]

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual_tokens = lexer.tokens

        parser = Parser(lexer, debug_print=True)
        parser.debug_print()
        parser.debug_print()
        parsing_success = parser.parse()

        # Assert
        self.assertListEqual(actual_tokens, expected_tokens)
        self.assertTrue(parsing_success)

    def test_without_function_definition(self):
        # Arrange
        input_string = "$ $ $ a = b; $"
        expected_tokens = [
            Token("$", TokenType.SEPARATOR),
            Token("$", TokenType.SEPARATOR),
            Token("$", TokenType.SEPARATOR),
            Token("a", TokenType.IDENTIFIER),
            Token("=", TokenType.OPERATOR),
            Token("b", TokenType.IDENTIFIER),
            Token(";", TokenType.SEPARATOR),
            Token("$", TokenType.SEPARATOR)
        ]

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual_tokens = lexer.tokens

        parser = Parser(lexer, debug_print=True)
        parser.debug_print()
        parser.debug_print()
        parsing_success = parser.parse()

        # Assert
        self.assertListEqual(actual_tokens, expected_tokens)
        self.assertTrue(parsing_success)

    def test_not_end_with_dollar_symbol(self):
        # Arrange
        input_string = "$ $ $ a = b; $xyz"
        expected_tokens = [
            Token("$", TokenType.SEPARATOR),
            Token("$", TokenType.SEPARATOR),
            Token("$", TokenType.SEPARATOR),
            Token("a", TokenType.IDENTIFIER),
            Token("=", TokenType.OPERATOR),
            Token("b", TokenType.IDENTIFIER),
            Token(";", TokenType.SEPARATOR),
            Token("$", TokenType.SEPARATOR),
            Token("xyz", TokenType.IDENTIFIER)
        ]

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual_tokens = lexer.tokens

        parser = Parser(lexer, debug_print=True)
        parser.debug_print()
        parser.debug_print()
        parsing_success = parser.parse()

        # Assert
        self.assertListEqual(actual_tokens, expected_tokens)
        self.assertFalse(parsing_success)

    def test_the_input_is_empty(self):
        # Arrange
        input_string = ""
        expected_tokens = []

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual_tokens = lexer.tokens

        parser = Parser(lexer, debug_print=True)
        parser.debug_print()
        parser.debug_print()
        parsing_success = parser.parse()

        # Assert
        self.assertListEqual(actual_tokens, expected_tokens)
        self.assertFalse(parsing_success)


if __name__ == '__main__':
    unittest.main()
