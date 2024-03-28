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

    def test_no_print_keyword(self):
        input_string = " $$ ( a + b ); $"
        expected_output= False

        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
    