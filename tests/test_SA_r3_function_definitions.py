import unittest
import os
from tests.helpers import write_to_file, get_result_from_parser


class FunctionDefinitionsTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_1fn_0params_0statements(self):
        # Arrange
        input_string = "$ function abc() { } $ $ $"
        expected_output = False

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_1fn_0params_1statement(self):
        # Arrange
        input_string = "$ function abc() { a = 1.1; } $ $ num = 1; $"
        expected_output = True

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_1fn_1param_1statement(self):
        # Arrange
        input_string = "$ function abc(amount real) { a = amount; } $ $ num = 1; $"
        expected_output = True

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_2fns_2params_2statements(self):
        # Arrange
        input_string = """
                    $ 
                        function move(x real, y real)
                        {
                            longitude = x;
                            latitude = y;
                        }

                        function scale(x integer, y integer)
                        {
                            width = width * x;
                            height = height * y;
                        }
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

    def test_missing_function_name(self):
        # Arrange
        input_string = "$ function () $ $ $"
        expected_output = False

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_missing_open_parenthesis(self):
        # Arrange
        input_string = "$ function abc) { } $ $ $"
        expected_output = False

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_missing_close_parenthesis(self):
        # Arrange
        input_string = "$ function abc( { } $ $ $"
        expected_output = False

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)


    def test_missing_body(self):
        # Arrange
        input_string = "$ function abc() $ $ $"
        expected_output = False

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
