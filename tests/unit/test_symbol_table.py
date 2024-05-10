import unittest
import os
from io import StringIO
from tests.unit.helpers import write_to_file, get_result_from_code_generator


class SymbolTableTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_variable_not_defined(self):
        # Arrange
        input_string = """
            $
            $
            $
                success = true;
            $
        """

        expected_output = ""

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_variable_already_defined(self):
        # Arrange
        input_string = """
            $
            $
                boolean success;
                boolean success;
            $
                success = true;
            $
        """

        expected_output = ""

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
