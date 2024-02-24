import os
import unittest
from common.enums import TokenType
from components.lexcical_analyzer import Lexer, Token


class IntegerTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_0point0(self):
        # Arrange
        input_string = "0.0"
        expected = Token(input_string, TokenType.REAL)

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual = lexer.tokens[0]

        # Assert
        self.assertEqual(actual, expected)

    def test_123point1(self):
        # Arrange
        input_string = "123.1"
        expected = Token(input_string, TokenType.REAL)

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual = lexer.tokens[0]

        # Assert
        self.assertEqual(actual, expected)

    def test_point_0(self):
        # Arrange
        input_string = ".0"

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual = lexer.tokens[0]

        # Assert
        self.assertEqual(actual.token_type, TokenType.UNKNOWN)

    def test_0_point(self):
        # Arrange
        input_string = "0."

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual = lexer.tokens[0]

        # Assert
        self.assertEqual(actual.token_type, TokenType.UNKNOWN)

if __name__ == '__main__':
    unittest.main()
