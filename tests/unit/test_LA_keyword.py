import unittest
import os
from common.enums import TokenType
from components.lexcical_analyzer import Lexer, Token


class OperatorTestCase(unittest.TestCase):

    SAMPLE_FILE_PATH = "tests/sample1.txt"
    KEYWORDS = ['function', 'integer', 'boolean', 'real', 'if', 'endif', 'else', 'return', 'print',
                'scan', 'while', 'endwhile', 'true', 'false']

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_keywords(self):
        
        for e in self.KEYWORDS:
            # Arrange
            expected_lexeme = e
            expected_tokentype = TokenType.KEYWORD

            with open(self.SAMPLE_FILE_PATH, 'w') as file:
                file.write(e)

             # Act
            lexer = Lexer(self.SAMPLE_FILE_PATH)
            actual = lexer.tokens[0]

            # Assert
            self.assertEqual(actual.token_type, expected_tokentype, f"Cannot recognize the keyword '{actual.lexeme}'")

    def test_not_a_keyword(self):
        # Arrange
        input_string = "iff fif "
        expected_tokens = [
            Token("iff", TokenType.IDENTIFIER),
            Token("fif", TokenType.IDENTIFIER)
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
