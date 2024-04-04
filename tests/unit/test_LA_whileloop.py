import os
import unittest
from common.enums import TokenType
from components.lexcical_analyzer import Lexer, Token


class WhileLoopTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_multilines_with_whitespaces(self):
        # Arrange
        input_string = """
            while (fahr <= upper) 
            {
                a = 23.00;
                b = 9;
            }
        """

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        expected_tokens = [
            Token("while", TokenType.KEYWORD),
            Token("(", TokenType.SEPARATOR),
            Token("fahr", TokenType.IDENTIFIER),
            Token("<=", TokenType.OPERATOR),
            Token("upper", TokenType.IDENTIFIER),
            Token(")", TokenType.SEPARATOR),
            Token("{", TokenType.SEPARATOR),
            Token("a", TokenType.IDENTIFIER),
            Token("=", TokenType.OPERATOR),
            Token("23.00", TokenType.REAL),
            Token(";", TokenType.SEPARATOR),
            Token("b", TokenType.IDENTIFIER),
            Token("=", TokenType.OPERATOR),
            Token("9", TokenType.INTEGER),
            Token(";", TokenType.SEPARATOR),
            Token("}", TokenType.SEPARATOR)
        ]

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual_tokens = lexer.tokens

        # Assert
        self.assertListEqual(actual_tokens, expected_tokens)

    def test_oneline_with_whitespaces(self):
        # Arrange
        input_string = "while (fahr <= upper) a = 23.00;"

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        expected_tokens = [
            Token("while", TokenType.KEYWORD),
            Token("(", TokenType.SEPARATOR),
            Token("fahr", TokenType.IDENTIFIER),
            Token("<=", TokenType.OPERATOR),
            Token("upper", TokenType.IDENTIFIER),
            Token(")", TokenType.SEPARATOR),
            Token("a", TokenType.IDENTIFIER),
            Token("=", TokenType.OPERATOR),
            Token("23.00", TokenType.REAL),
            Token(";", TokenType.SEPARATOR),
        ]

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual_tokens = lexer.tokens

        # Assert
        self.assertListEqual(actual_tokens, expected_tokens)

    def test_oneline_without_whitespaces(self):
        # Arrange
        input_string = "while(fahr<=upper)a=23.00;"

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(input_string)

        expected_tokens = [
            Token("while", TokenType.KEYWORD),
            Token("(", TokenType.SEPARATOR),
            Token("fahr", TokenType.IDENTIFIER),
            Token("<=", TokenType.OPERATOR),
            Token("upper", TokenType.IDENTIFIER),
            Token(")", TokenType.SEPARATOR),
            Token("a", TokenType.IDENTIFIER),
            Token("=", TokenType.OPERATOR),
            Token("23.00", TokenType.REAL),
            Token(";", TokenType.SEPARATOR),
        ]

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        actual_tokens = lexer.tokens

        # Assert
        self.assertListEqual(actual_tokens, expected_tokens)


if __name__ == '__main__':
    unittest.main()
