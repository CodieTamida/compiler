import unittest
import os
from common.enums import TokenType
from components.lexcical_analyzer import Lexer, Token
from components.syntax_analyzer import Parser


class StatementTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_1id(self):
        # Arrange
        input_string = "$ a $"
        expected_tokens = [
            Token("$", TokenType.SEPARATOR),
            Token("a", TokenType.IDENTIFIER),
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

    def test_2ids_1op(self):
        # Arrange
        input_string = "$ a = b; $"
        expected_tokens = [
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

    def test_3ids_2ops(self):
        # Arrange
        input_string = "$ a = b + c; $"
        expected_tokens = [
            Token("$", TokenType.SEPARATOR),
            Token("a", TokenType.IDENTIFIER),
            Token("=", TokenType.OPERATOR),
            Token("b", TokenType.IDENTIFIER),
            Token("+", TokenType.OPERATOR),
            Token("c", TokenType.IDENTIFIER),
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

    def test_4ids_3ops(self):
        # Arrange
        input_string = "$ a = b + c - d; $"
        expected_tokens = [
            Token("$", TokenType.SEPARATOR),
            Token("a", TokenType.IDENTIFIER),
            Token("=", TokenType.OPERATOR),
            Token("b", TokenType.IDENTIFIER),
            Token("+", TokenType.OPERATOR),
            Token("c", TokenType.IDENTIFIER),
            Token("-", TokenType.OPERATOR),
            Token("d", TokenType.IDENTIFIER),
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
        parsing_success = parser.parse()

        # Assert
        self.assertListEqual(actual_tokens, expected_tokens)
        self.assertTrue(parsing_success)

    def test_4ids_3ops_mul_div(self):
        # Arrange
        input_string = "$ a = b * c - d; $"
        expected_tokens = [
            Token("$", TokenType.SEPARATOR),
            Token("a", TokenType.IDENTIFIER),
            Token("=", TokenType.OPERATOR),
            Token("b", TokenType.IDENTIFIER),
            Token("*", TokenType.OPERATOR),
            Token("c", TokenType.IDENTIFIER),
            Token("-", TokenType.OPERATOR),
            Token("d", TokenType.IDENTIFIER),
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
        parsing_success = parser.parse()

        # Assert
        self.assertListEqual(actual_tokens, expected_tokens)
        self.assertTrue(parsing_success)

    def test_2ids_2ops_1boolean(self):
        # Arrange
        input_string = "$ a = b - true; $"
        expected_tokens = [
            Token("$", TokenType.SEPARATOR),
            Token("a", TokenType.IDENTIFIER),
            Token("=", TokenType.OPERATOR),
            Token("b", TokenType.IDENTIFIER),
            Token("-", TokenType.OPERATOR),
            Token("true", TokenType.KEYWORD),
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
        parsing_success = parser.parse()

        # Assert
        self.assertListEqual(actual_tokens, expected_tokens)
        self.assertTrue(parsing_success)

    def test_2ids_2ops_1negative_int(self):
        # Arrange
        input_string = "$ a = b - -3; $"
        expected_tokens = [
            Token("$", TokenType.SEPARATOR),
            Token("a", TokenType.IDENTIFIER),
            Token("=", TokenType.OPERATOR),
            Token("b", TokenType.IDENTIFIER),
            Token("-", TokenType.OPERATOR),
            Token("-", TokenType.OPERATOR),
            Token("3", TokenType.INTEGER),
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
        parsing_success = parser.parse()

        # Assert
        self.assertListEqual(actual_tokens, expected_tokens)
        self.assertTrue(parsing_success)

    def test_2ids_2ops_1real(self):
        # Arrange
        input_string = "$ a = b - 3.1; $"
        expected_tokens = [
            Token("$", TokenType.SEPARATOR),
            Token("a", TokenType.IDENTIFIER),
            Token("=", TokenType.OPERATOR),
            Token("b", TokenType.IDENTIFIER),
            Token("-", TokenType.OPERATOR),
            Token("3.1", TokenType.REAL),
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
        parsing_success = parser.parse()

        # Assert
        self.assertListEqual(actual_tokens, expected_tokens)
        self.assertTrue(parsing_success)

    def test_invalid_missing_id(self):
        # Arrange
        input_string = "$ a = b + ; $"
        expected_tokens = [
            Token("$", TokenType.SEPARATOR),
            Token("a", TokenType.IDENTIFIER),
            Token("=", TokenType.OPERATOR),
            Token("b", TokenType.IDENTIFIER),
            Token("+", TokenType.OPERATOR),
            Token(";", TokenType.SEPARATOR),
            Token("$", TokenType.SEPARATOR),
        ]

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual_tokens = lexer.tokens

        parser = Parser(lexer, debug_print=True)
        parser.debug_print()
        parsing_success = parser.parse()

        # Assert
        self.assertListEqual(actual_tokens, expected_tokens)
        self.assertFalse(parsing_success)


if __name__ == '__main__':
    unittest.main()
