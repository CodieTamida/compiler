import unittest
import os
from tests.unit.helpers import write_to_file, get_result_from_parser


class AssignTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_0_statements(self):
        # Arrange
        input_string = "$ $ $ $"
        expected_output = False

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_1_statement(self):
        # Arrange
        input_string = """
                    $                         
                    $ 
                    $
                        num = 1;
                    $
                    """
        expected_output = True

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_2_statements(self):
        # Arrange
        input_string = """
                    $                         
                    $ 
                    $
                        num = 1;
                        num = 2;
                    $
                    """
        expected_output = True

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_3_statements(self):
        # Arrange
        input_string = """
                    $                         
                    $ 
                    $
                        num = 1;
                        num = 2;
                        num = 3;
                    $
                    """
        expected_output = True

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_4_statements(self):
        # Arrange
        input_string = """
                    $                         
                    $ 
                    $
                        num = 1;
                        num = 2;
                        num = 3;
                        num = 4;
                    $
                    """
        expected_output = True

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
