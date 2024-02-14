import unittest
from common.enums import TokenType
from components.lexcical_analyzer import tokenize


class OperatorTestCase(unittest.TestCase):

    def test_addition_operator(self):
        # Arrange
        input_str = "+"
        expected_tokens = (
            (TokenType.OPERATOR, "+"),
        )

        # Act
        actual_tokens = tokenize(input_str)

        # Assert
        self.assertEqual(actual_tokens, expected_tokens)

    def test_subtraction_operator(self):
        # Arrange
        input_str = "-"
        expected_tokens = (
            (TokenType.OPERATOR, "+"),
        )

        # Act
        actual_tokens = tokenize(input_str)

        # Assert
        self.assertEqual(actual_tokens, expected_tokens)

    def test_multiplication_operator(self):
        # Arrange
        input_str = "*"
        expected_tokens = (
            (TokenType.OPERATOR, "+"),
        )

        # Act
        actual_tokens = tokenize(input_str)

        # Assert
        self.assertEqual(actual_tokens, expected_tokens)

    def test_division_operator(self):
        # Arrange
        input_str = "/"
        expected_tokens = (
            (TokenType.OPERATOR, "+"),
        )

        # Act
        actual_tokens = tokenize(input_str)

        # Assert
        self.assertEqual(actual_tokens, expected_tokens)


if __name__ == '__main__':
    unittest.main()
