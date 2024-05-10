import unittest
import os
from io import StringIO
from tests.unit.helpers import write_to_file, get_result_from_code_generator


class WhileTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_simple(self):
        # Arrange
        input_string = """
            $
            $
                integer i;
            $
                i = 0;
                while(i < 10)
                    i = i + 1;
                endwhile
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 0\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("LABEL\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHI 10\n")
        string_builder.write("LES\n")
        string_builder.write("JUMP0 13\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHI 1\n")
        string_builder.write("A\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("JUMP 3\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_nested_2(self):
        # Arrange
        input_string = """
            $
            $
                integer i, j;
            $
                i = 0;
                while(i < 10)
                {
                    j = 20;
                    while(j > 0)
                        j = j - 2;
                    endwhile
                    i = i + 1;
                }                    
                endwhile
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 0\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("LABEL\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHI 10\n")
        string_builder.write("LES\n")
        string_builder.write("JUMP0 25\n")
        string_builder.write("PUSHI 20\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("LABEL\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("PUSHI 0\n")
        string_builder.write("GRT\n")
        string_builder.write("JUMP0 20\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("S\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("JUMP 10\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHI 1\n")
        string_builder.write("A\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("JUMP 3\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_nested_3(self):
        # Arrange
        input_string = """
            $
            $
                integer i, j, k;
            $
                i = 0;
                while(i <= 10)
                {
                    j = 20;
                    while(j => 0)
                    {
                        k = i - j; 
                        while(k != 0)
                        {
                            print(k);
                        } 
                        endwhile
                        j = j - 2;
                    }                        
                    endwhile
                    i = i + 1;
                }                    
                endwhile
            $
        """

        string_builder = StringIO()
        string_builder.write("PUSHI 0\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("LABEL\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHI 10\n")
        string_builder.write("LEQ\n")
        string_builder.write("JUMP0 37\n")
        string_builder.write("PUSHI 20\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("LABEL\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("PUSHI 0\n")
        string_builder.write("GEQ\n")
        string_builder.write("JUMP0 32\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("S\n")
        string_builder.write("POPM 5002\n")
        string_builder.write("LABEL\n")
        string_builder.write("PUSHM 5002\n")
        string_builder.write("PUSHI 0\n")
        string_builder.write("NEQ\n")
        string_builder.write("JUMP0 27\n")
        string_builder.write("PUSHM 5002\n")
        string_builder.write("SOUT\n")
        string_builder.write("JUMP 19\n")
        string_builder.write("PUSHM 5001\n")
        string_builder.write("PUSHI 2\n")
        string_builder.write("S\n")
        string_builder.write("POPM 5001\n")
        string_builder.write("JUMP 10\n")
        string_builder.write("PUSHM 5000\n")
        string_builder.write("PUSHI 1\n")
        string_builder.write("A\n")
        string_builder.write("POPM 5000\n")
        string_builder.write("JUMP 3\n")
        expected_output = string_builder.getvalue()

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_code_generator(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
