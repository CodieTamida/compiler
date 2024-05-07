import unittest
import os
from io import StringIO
from tests.unit.helpers import write_to_file, get_result_from_code_generator


class ScanTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_1_ID(self):

        input_string = """
            $
            $
                integer a;
            $
                scan(a);
            $
        """
        string_builder = StringIO()
        string_builder.write("SIN\n")
        string_builder.write("POPM 5000\n")
        expected_output = string_builder.getvalue()

         # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)
    def test_multiple_IDs(self):
        input_string = """
            $
            $
            integer a, b, c;
            $
            scan( a,b, c);
            $
        """
        string_builder = StringIO()
        string_builder.write("SIN\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("SIN\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("SIN\n")
        string_builder.write("POPM 5002\n")
        expected_output = string_builder.getvalue()

         # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_ID_not_declared(self):
        input_string = """
            $
            $
            integer a;
            $
            scan ( a, b);
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