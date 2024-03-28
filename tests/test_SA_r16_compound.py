import unittest
import os
from tests.helpers import write_to_file, get_result_from_parser


class CompoundTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self) -> None:
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self) -> None:
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    
    def test_compound(self):
        # Arrange
        input_string = "$$$ { a = b + z; } $"
        expected_output = True

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)


    def test_compound_no_closing_brace(self):
        input_string = "$$$ { a- 2; $"
        expected_output= False

        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        self.assertEqual(actual_output, expected_output)

    def test_compound_no_opening_brace(self):
        input_string = "$$$  a - -5;}$"
        expected_output= False

        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        self.assertEqual(actual_output, expected_output)

    def test_compound_no_braces(self):
        input_string = "$$$  a - c; $"
        expected_output= False

        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        self.assertEqual(actual_output, expected_output)



if __name__ == '__main__':
    unittest.main()
    
