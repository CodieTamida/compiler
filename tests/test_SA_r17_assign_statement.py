import unittest
import os
from tests.helpers import write_to_file, get_result_from_parser


class AssignTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_2ids_1op(self):
        # Arrange
        input_string = "$ $ $ a = b; $"
        expected_output = True

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_3ids_2ops(self):
        # Arrange
        input_string = "$ $ $ a = b + c; $"
        expected_output = True

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_4ids_3ops(self):
        # Arrange
        input_string = "$ $ $ a = b + c - d; $"
        expected_output = True

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_4ids_3ops_mul_div(self):
        # Arrange
        input_string = "$ $ $ a = b * c - d; $"
        expected_output = True

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_2ids_2ops_1boolean(self):
        # Arrange
        input_string = "$ $ $ a = b - true; $"
        expected_output = True

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_2ids_2ops_1negative_int(self):
        # Arrange
        input_string = "$ $ $ a = b - -3; $"
        expected_output = True

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_2ids_2ops_1real(self):
        # Arrange
        input_string = "$ $ $ a = b - 3.1; $"
        expected_output = True

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_missing_a_factor(self):
        # Arrange
        input_string = "$ $ $ a = b + ; $"
        expected_output = False

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_no_assignment_operator(self):
        # Arrange
        input_string = "$ $ $ a; $"
        expected_output = False

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_missing_semicolon(self):
        # Arrange
        input_string = "$ $ $ a = b $"
        expected_output = False

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
