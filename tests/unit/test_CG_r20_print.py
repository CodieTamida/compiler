import unittest
import os
from io import StringIO
from tests.unit.helpers import write_to_file, get_result_from_code_generator


class PrintTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_1_expression(self):

        input_string = """
            $
            $
                integer a, b;
            $
                print(a + b);
            $
        """
        string_builder = StringIO()
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("A\n")
        string_builder.write("SOUT\n")
        expected_output = string_builder.getvalue()

         # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_compound_expressions(self):
        input_string = """
            $
            $
                integer a, b, c;
            $
                print(a + b * c);
            $
        """
        string_builder = StringIO()
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("PUSHM 5002\n")
        string_builder.write("M\n")
        string_builder.write("A\n")
        string_builder.write("SOUT\n")
        expected_output = string_builder.getvalue()

         # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)


    def test_compound_expressions_all_signs(self):
        input_string = """
            $
            $
                integer a, b, c, d;
            $
                print(a + b * c / d - a);
            $
        """
        string_builder = StringIO()
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("PUSHM 5002\n")
        string_builder.write("M\n")
        string_builder.write("PUSHM 5003\n")
        string_builder.write("D\n")
        string_builder.write("A\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("S\n")
        string_builder.write("SOUT\n")
        expected_output = string_builder.getvalue()

         # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()