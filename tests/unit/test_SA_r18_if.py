import unittest
import os
from tests.unit.helpers import write_to_file, get_result_from_parser


class IfTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"

    def setUp(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def tearDown(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

    def test_if_no_else(self):
        input_string = "$ $ $ if (a == b ) return c; endif $"
        expected_output = True

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)
    
    def test_if_else(self):
        input_string = "$ $ $ if (a == b ) return c; else return 85; endif $"
        expected_output = True

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_nested_if(self):
        input_string = """
            $ $ $ 
                if (a == b) 
                    if (a == b) 
                        if (a == b) {
                            a = b + 1;
                            if (a == b) 
                                return c;
                            else
                                return d;
                            endif
                        }
                        else {
                            b = b + 3;
                            a = a * b;

                            [* <Primary> ::= <Identifier> ( <IDs> ) *]
                            if (average(a, b, c, d, e, f) < 100.512)
                                return a;
                            else
                                return c;
                            endif
                        }
                        endif
                    endif
                endif
            $
            """
        expected_output = True

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_if_no_if(self):
        input_string = "$ $ $ (a == b ) return c; endif $"
        expected_output = False

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)
    
    def test_if_no_endif(self):
        input_string = "$ $ $ if (a == b ) return c; $"
        expected_output = False

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_if_no_open_paren(self):
        input_string = "$ $ $ if a == b ) return c; endif $"
        expected_output = False

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)

    def test_if_no_close_paren(self):
        input_string = "$ $ $ if (a == b  return c; endif $"
        expected_output = False

        # Act
        write_to_file(self.SAMPLE_FILE_PATH, input_string)
        actual_output = get_result_from_parser(self.SAMPLE_FILE_PATH)

        # Assert
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()