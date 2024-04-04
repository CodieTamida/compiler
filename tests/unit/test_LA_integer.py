import unittest
import os
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

    def test_single_digit(self):
        # Arrange
        input_string = "0"
        expected = Token(input_string, TokenType.INTEGER)

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual = lexer.tokens[0]

        # Assert
        self.assertEqual(actual, expected)

    def test_multiple_digits(self):
        # Arrange
        input_string = "123"
        expected = Token(input_string, TokenType.INTEGER)

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual = lexer.tokens[0]

        # Assert
        self.assertEqual(actual, expected)

    def test_not_a_number(self):
        # Arrange
        input_string = "abc"

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual = lexer.tokens[0]

        # Assert
        self.assertNotEqual(actual.token_type, TokenType.INTEGER)


if __name__ == '__main__':
    unittest.main()
