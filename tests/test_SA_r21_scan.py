import unittest
import os
from tests.helpers import write_to_file, get_result_from_parser

class PrintTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_scan(self):
        input_string = " $$$ scan( abc_x123 ); $"
        expected_output= True

        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        self.assertEqual(actual_output, expected_output)

    def test_scan_with_multiple_ids(self):
        input_string = "$$$ scan (x , we_12, hello_world); $"
        expected_output = True

        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        self.assertEqual(actual_output, expected_output)

    def test_scan_no_scan_keyword(self):
        input_string = " $$$ (abcx_123); $"
        expected_output = False

        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        self.assertEqual(actual_output, expected_output)
    
    def test_scan_no_id(self):
        input_string = "$$$ scan ( ); $"
        expected_output = False

        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        self.assertEqual(actual_output, expected_output) 

    def test_print_incorrect_id(self):
        input_string = " $$$ scan ( _e3erts ); $"
        expected_output = False

        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        self.assertEqual(actual_output, expected_output)

    def test_print_no_open_paren(self):
        input_string = " $$$ scan 4 + x); $"
        expected_output = False

        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        self.assertEqual(actual_output, expected_output)

    def test_no_close_paren(self):
        input_string = "$$$ scan (x; $"
        expected_output = False

        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        self.assertEqual(actual_output, expected_output)

    def test_scan_no_semicolon(self):
        input_string = "$$$ scan (hello) $"
        expected_output = False

        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        self.assertEqual(actual_output, expected_output)
if __name__ == '__main__':
    unittest.main()