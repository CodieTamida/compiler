import unittest
import os
from io import StringIO
from tests.unit.helpers import write_to_file, get_result_from_code_generator


class AssignTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_integer(self):
        # Arrange
        input_string = """
            $
            $
                integer a, b, c;
            $
                a = 128;
                b = -256;
                c = 512;
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 128\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("PUSHI -256\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHI 512\n")
        string_builder.write("POPM 5002\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_boolean(self):
        # Arrange
        input_string = """
            $
            $
                boolean success;
                boolean failed;
            $
                success = true;
                failed = false;
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 1\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("PUSHI 0\n")
        string_builder.write("POPM 5001\n")
        expected_output = string_builder.getvalue()

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

    

    def test_multiplication_2(self):
        # Arrange
        input_string = """
            $
            $
                integer a, b, sum;
            $
                a = 1;
                b = 2;
                sum = a * b * (8 * 2);
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 1\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("M\n")
        string_builder.write("POPM 5002\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        # self.assertEqual(actual_output, expected_output)

    def test_multiplication_datatypes_mismatch(self):
        # Arrange
        input_string = """
            $
            $
                integer a, sum;
                boolean b;                
            $
                a = 1;
                b = true;
                sum = 1 * true  ;
            $
        """

        expected_output = ""

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_division_datatypes_mismatch(self):
        # Arrange
        input_string = """
            $
            $
                integer a, sum;
                boolean b;                
            $
                a = 1;
                b = true;
                sum = 1 / true  ;
            $
        """

        expected_output = ""

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)


    

    @unittest.skip
    def test_1(self):
        # Arrange
        input_string = """
            [* this is comment for this sample code for assignment 3 *]
            $
            [* NO function definitions *]
            $
                integer i, max, sum; [* declarations *]
                real average;
            $
                sum = 0;
                i = 1;
                scan (max);
                while (i < max) {
                    sum = sum + i;
                    i = i + 1;
                }
                endwhile
                print (sum + max);
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
