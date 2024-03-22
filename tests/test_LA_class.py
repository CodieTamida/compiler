import unittest
import os
from common.enums import TokenType
from components.lexcical_analyzer import Lexer, Token


class LexerTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_get_next_token(self):
        # Arrange
        input_string = "function convertx()[** ]* ]this is comment*]{ }"
        expected_tokens = [
            Token("function", TokenType.KEYWORD),
            Token("convertx", TokenType.IDENTIFIER),
            Token("(", TokenType.SEPARATOR),
            Token(")", TokenType.SEPARATOR),
            Token("{", TokenType.SEPARATOR),
            Token("}", TokenType.SEPARATOR)
        ]

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual_tokens = list()

        token = lexer.get_next_token()

        while token:
            actual_tokens.append(token)
            token = lexer.get_next_token()

        # Assert
        self.assertListEqual(actual_tokens, expected_tokens)


if __name__ == '__main__':
    unittest.main()
