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

    def test_arithmetic_expression_to_intvar_1(self):
        # Arrange
        input_string = """
            $
            $
                integer a;
            $
                a = (5 + 7);
            $
        """
        string_builder = StringIO()
        string_builder.write("PUSHI 5\n")
        string_builder.write("PUSHI 7\n")
        string_builder.write("A\n")
        string_builder.write("POPM 5000\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_arithmetic_expression_to_intvar_2(self):
        # Arrange
        input_string = """
            $
            $
                integer a, b;                
            $
                a = (5 + 7) / b;
            $
        """
        string_builder = StringIO()
        string_builder.write("PUSHI 5\n")
        string_builder.write("PUSHI 7\n")
        string_builder.write("A\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("D\n")
        string_builder.write("POPM 5000\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_boolvalue_in_parentheses_to_boolvar(self):
        # Arrange
        input_string = """
            $
            $
                boolean a;
            $
                a = ((((true))));
            $
        """
        string_builder = StringIO()
        string_builder.write("PUSHI 1\n")
        string_builder.write("POPM 5000\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_intvar_to_intvar(self):
        # Arrange
        input_string = """
            $
            $
                integer a, b;
            $
                a = b;
            $
        """
        string_builder = StringIO()
        string_builder.write("PUSHM 5001\n")
        string_builder.write("POPM 5000\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_real_number_not_allowed(self):
        # Arrange
        input_string = """
            $
            $
                integer a;
            $
                a = 5.5;
            $
        """
        expected_output = ""

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_int_to_boolvar_not_allowed(self):
        # Arrange
        input_string = """
            $
            $
                boolean a;
            $
                a = 5;
            $
        """
        expected_output = ""

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_intvar_to_boolvar_not_allowed(self):
        # Arrange
        input_string = """
            $
            $
                integer a;
                boolean b;
            $
                b = a;
            $
        """
        expected_output = ""

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_boolvar_to_intvar_not_allowed(self):
        # Arrange
        input_string = """
            $
            $
                integer a;
                boolean b;
            $
                a = b;
            $
        """
        expected_output = ""

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_bool_to_intvar_not_allowed(self):
        # Arrange
        input_string = """
            $
            $
                integer a;
            $
                a = true;
            $
        """
        expected_output = ""

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_arithmetic_expression_to_boolvar_not_allowed(self):
        # Arrange
        input_string = """
            $
            $
                boolean a;
            $
                a = (5 + 7);
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
