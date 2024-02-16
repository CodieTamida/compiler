import unittest
import os
from common.enums import TokenType
from components.lexcical_analyzer import Lexer


class LexerTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

        string_to_write = """
        function xyz(int x, int y, int width, int height) {
            while (fahr <= upper) {
                a = 23.00;
                b = 9;
            }
            return true;
        }
        """

        with open(self.SAMPLE_FILE_PATH, 'w') as file:
            file.write(string_to_write)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_open_file(self):
        # Arrange

        # Act
        lexer = Lexer(self.SAMPLE_FILE_PATH)
        print(lexer.content)
        for i in range(38):
            token = lexer.next_token()
            print(token.lexeme, token.token_type)
        
        # Assert
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
