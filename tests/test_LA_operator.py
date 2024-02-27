import unittest
import os
from common.enums import TokenType
from components.lexcical_analyzer import Lexer, Token


class OperatorTestCase(unittest.TestCase):

    SAMPLE_FILE_PATH = "tests/operator_test.txt"
    SIMPLE_OPERATORS = {'>', '<', '=', '+', '-', '*', '/'}
    COMPOUND_OPERATORS = {'==', '!=', '<=', '=>'}

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_operators(self):
        operators = self.SIMPLE_OPERATORS | self.COMPOUND_OPERATORS

        for op in operators:
            # Arrange
            expected_lexeme = op
            expected_tokentype = TokenType.OPERATOR

            with open(self.SAMPLE_FILE_PATH, 'w') as file:
                file.write(op)

             # Act
            lexer = Lexer(self.SAMPLE_FILE_PATH)
            actual = lexer.tokens[0]

            # Assert
            self.assertEqual(actual.lexeme, expected_lexeme)
            self.assertEqual(actual.token_type, expected_tokentype)

    def test_illegal_operators(self):
        # Arrange
        input_string = "?% !% !!% ! % ###"
        expected_tokens = [
            Token("?%", TokenType.UNKNOWN),
            Token("!%", TokenType.UNKNOWN),
            Token("!!%", TokenType.UNKNOWN),
            Token("!", TokenType.UNKNOWN),
            Token("%", TokenType.UNKNOWN),
            Token("###", TokenType.UNKNOWN)
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
