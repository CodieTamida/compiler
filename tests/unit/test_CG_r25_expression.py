import unittest
import os
from io import StringIO
from tests.unit.helpers import write_to_file, get_result_from_code_generator


class ExpressionTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_addition_two_ids(self):
        # Arrange
        input_string = """
            $
            $
                integer a, b, c;
            $
                a = 1;
                b = 2;
                c = a + b;
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 1\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("A\n")
        string_builder.write("POPM 5002\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_addition_id_integer(self):
        # Arrange
        input_string = """
            $
            $
                integer a, b;
            $
                a = 1;
                b = 2 + a;
                b = a + 3;
                a = 5 + b;
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 1\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("A\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHI 3\n")
        string_builder.write("A\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHI 5\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("A\n")
        string_builder.write("POPM 5000\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_subtraction_two_ids(self):
        # Arrange
        input_string = """
            $
            $
                integer a, b, c;
            $
                a = 1;
                b = 2;
                c = a - b;
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 1\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("S\n")
        string_builder.write("POPM 5002\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_subtraction_id_integer(self):
        # Arrange
        input_string = """
            $
            $
                integer a, b;
            $
                a = 1;
                b = 2 - a;
                b = a - 3;
                a = 5 - b;
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 1\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("S\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHI 3\n")
        string_builder.write("S\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHI 5\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("S\n")
        string_builder.write("POPM 5000\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_multiplication_two_ids(self):
        # Arrange
        input_string = """
            $
            $
                integer a, b, c;
            $
                a = 1;
                b = 2;
                c = a * b;
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 1\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("M\n")
        string_builder.write("POPM 5002\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_multiplication_id_integer(self):
        # Arrange
        input_string = """
            $
            $
                integer a, b;
            $
                a = 1;
                b = 2 * a;
                b = a * 3;
                a = 5 * b;
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 1\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("M\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHI 3\n")
        string_builder.write("M\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHI 5\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("M\n")
        string_builder.write("POPM 5000\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_division_two_ids(self):
        # Arrange
        input_string = """
            $
            $
                integer a, b, c;
            $
                a = 1;
                b = 2;
                c = a / b;
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 1\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("D\n")
        string_builder.write("POPM 5002\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_division_id_integer(self):
        # Arrange
        input_string = """
            $
            $
                integer a, b;
            $
                a = 1;
                b = 2 / a;
                b = a / 3;
                a = 5 / b;
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 1\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("D\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHI 3\n")
        string_builder.write("D\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHI 5\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("D\n")
        string_builder.write("POPM 5000\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_2ids_2integers(self):
        # Arrange
        input_string = """
            $
            $
                integer a, b, sum;
            $
                a = 1;
                b = 2;
                sum = a * b * 8 * 2;
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 1\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("M\n")
        string_builder.write("PUSHI 8\n")
        string_builder.write("M\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("M\n")
        string_builder.write("POPM 5002\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_many_expressions(self):
        # Arrange
        input_string = """
            $
            $
                integer a, b, sum;
            $
                a = 1;
                b = 2;
                sum = a * (b + 8) / (2 - a);
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 1\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("PUSHI 8\n")
        string_builder.write("A\n")
        string_builder.write("M\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("S\n")
        string_builder.write("D\n")
        string_builder.write("POPM 5002\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_nested(self):
        # Arrange
        input_string = """
            $
            $
                integer a, b, sum;
            $
                a = 1;
                b = 2;
                sum = a * (9 / 3 * (a - b)) - 2);
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 1\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHI 9\n")
        string_builder.write("PUSHI 3\n")
        string_builder.write("D\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("S\n")
        string_builder.write("M\n")
        string_builder.write("M\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("S\n")
        string_builder.write("POPM 5002\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_boolean_addition_not_allowed(self):
        # Arrange
        input_string = """
            $
            $
                integer a;            
            $
                a = 1 + true;
            $
        """

        expected_output = ""

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_expression_with_parenthesis(self):
        # Arrange
        input_string = """
            $
            $
                integer a, b, sum;
            $
                a = 1;
                b = 2;
                sum = a * (b + 8);
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 1\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("PUSHM 5000\n")
        
        string_builder.write("PUSHM 5001\n")
        string_builder.write("PUSHI 8\n")
        string_builder.write("A\n")
        string_builder.write("M\n")
        string_builder.write("POPM 5002\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_boolean_subtraction_not_allowed(self):
        # Arrange
        input_string = """
            $
            $
                integer a;            
            $
                a = 1 - true;
            $
        """

        expected_output = ""

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_boolean_multiplication_not_allowed(self):
        # Arrange
        input_string = """
            $
            $
                integer a;            
            $
                a = 1 * true;
            $
        """

        expected_output = ""

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_boolean_division_not_allowed(self):
        # Arrange
        input_string = """
            $
            $
                integer a;            
            $
                a = 1 / true;
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
