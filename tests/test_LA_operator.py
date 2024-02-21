import unittest
import os
from common.enums import TokenType
from components.lexcical_analyzer import Lexer


class OperatorTestCase(unittest.TestCase):

    SAMPLE_FILE_PATH = "tests/operator_test.txt"
    SIMPLE_OPERATORS = {'>', '<', '=', '+', '-', '*', '/'}
    COMPOUND_OPERATORS = {'==', '!=', '<=', '=>'}

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

        str1 = ' '.join(self.SIMPLE_OPERATORS)
        str2 = ' '.join(self.COMPOUND_OPERATORS)
        string_to_write = str1 + str2

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(string_to_write)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_operators(self):
        # Arrange
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        expected_len = len(self.SIMPLE_OPERATORS) + \
            len(self.COMPOUND_OPERATORS)

        # Act & Assert
        actual_len = 0
        while lexer.has_token():
            token = lexer.next_token()
            actual_len += 1
            self.assertEqual(token.token_type, TokenType.OPERATOR)

        self.assertEqual(actual_len, expected_len)


if __name__ == '__main__':
    unittest.main()
