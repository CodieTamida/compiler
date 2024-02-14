import unittest
from common.enums import TokenType
from components.lexcical_analyzer import tokenize


class WhileLoopTestCase(unittest.TestCase):

    def test_multilines_with_whitespaces(self):
        # Arrange
        input_str = """
            while (fahr <= upper) 
            {
                a = 23.00;
                b = 9;
            }
        """

        expected_tokens = (
            (TokenType.KEYWORD, "while"),
            (TokenType.SEPARATOR, "("),
            (TokenType.IDENTIFIER, "fahr"),
            (TokenType.OPERATOR, "<="),
            (TokenType.IDENTIFIER, "upper"),
            (TokenType.SEPARATOR, ")"),
            (TokenType.SEPARATOR, "{"),
            (TokenType.IDENTIFIER, "a"),
            (TokenType.OPERATOR, "="),
            (TokenType.REAL, "23.00"),
            (TokenType.SEPARATOR, ";"),
            (TokenType.IDENTIFIER, "b"),
            (TokenType.OPERATOR, "="),
            (TokenType.REAL, "9"),
            (TokenType.SEPARATOR, ";"),
            (TokenType.SEPARATOR, "}"),
        )

        # Act
        actual_tokens = tokenize(input_str)

        # Assert
        self.assertEqual(actual_tokens, expected_tokens)

    def test_oneline_with_whitespaces(self):
        # Arrange
        input_str = "while (fahr <= upper) a = 23.00;"

        expected_tokens = (
            (TokenType.KEYWORD, "while"),
            (TokenType.SEPARATOR, "("),
            (TokenType.IDENTIFIER, "fahr"),
            (TokenType.OPERATOR, "<="),
            (TokenType.IDENTIFIER, "upper"),
            (TokenType.SEPARATOR, ")"),
            (TokenType.IDENTIFIER, "a"),
            (TokenType.OPERATOR, "="),
            (TokenType.REAL, "23.00"),
            (TokenType.SEPARATOR, ";")
        )

        # Act
        actual_tokens = tokenize(input_str)

        # Assert
        self.assertEqual(actual_tokens, expected_tokens)

    def test_oneline_without_whitespaces(self):
        # Arrange
        input_str = "while(fahr<=upper)a=23.00;"

        expected_tokens = (
            (TokenType.KEYWORD, "while"),
            (TokenType.SEPARATOR, "("),
            (TokenType.IDENTIFIER, "fahr"),
            (TokenType.OPERATOR, "<="),
            (TokenType.IDENTIFIER, "upper"),
            (TokenType.SEPARATOR, ")"),
            (TokenType.IDENTIFIER, "a"),
            (TokenType.OPERATOR, "="),
            (TokenType.REAL, "23.00"),
            (TokenType.SEPARATOR, ";")
        )

        # Act
        actual_tokens = tokenize(input_str)

        # Assert
        self.assertEqual(actual_tokens, expected_tokens)


if __name__ == '__main__':
    unittest.main()
