import unittest
import os
from common.enums import TokenType
from components.lexcical_analyzer import Lexer, Token


class IdentifierTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_valid_identifiers(self):
        # Arrange
        input_string = "i i_ i8 index i_n_d_e_x index_123 index_ i____"
        expected_tokens = [
            Token("i", TokenType.IDENTIFIER),
            Token("i_", TokenType.IDENTIFIER),
            Token("i8", TokenType.IDENTIFIER),
            Token("index", TokenType.IDENTIFIER),
            Token("i_n_d_e_x", TokenType.IDENTIFIER),
            Token("index_123", TokenType.IDENTIFIER),
            Token("index_", TokenType.IDENTIFIER),
            Token("i____", TokenType.IDENTIFIER)
        ]

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual_tokens = lexer.tokens

        # Assert
        self.assertListEqual(actual_tokens, expected_tokens)

    def test_illegal_identifiers(self):
        # Arrange
        input_string = "1index _index #index @index _ __"
        expected_tokens = [
            Token("1index", TokenType.UNKNOWN),
            Token("_index", TokenType.UNKNOWN),
            Token("#index", TokenType.UNKNOWN),
            Token("@index", TokenType.UNKNOWN),
            Token("_", TokenType.UNKNOWN),
            Token("__", TokenType.UNKNOWN)
        ]

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual_tokens = lexer.tokens

        # Assert
        self.assertListEqual(actual_tokens, expected_tokens)


if __name__ == '__main__':
    unittest.main()
