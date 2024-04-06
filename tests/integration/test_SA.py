import unittest
import os
from components.lexcical_analyzer import Lexer, Token
from tests.integration.helpers import write_to_file, read_tokens_from_lexer_output, read_tokens_from_parser_output, run_command


class SyntaxAnalyzerTestCase(unittest.TestCase):
    SAMPLE_FILE_PATH = "tests/sample1.txt"
    LEXER_OUTPUT_PATH = "tests/lexer_output.txt"
    PARSER_OUTPUT_PATH = "tests/parser_output.txt"

    def clean_up(self):
        if os.path.exists(self.SAMPLE_FILE_PATH):
            os.remove(self.SAMPLE_FILE_PATH)

        if os.path.exists(self.LEXER_OUTPUT_PATH):
            os.remove(self.LEXER_OUTPUT_PATH)
        
        if os.path.exists(self.PARSER_OUTPUT_PATH):
            os.remove(self.PARSER_OUTPUT_PATH)

    def setUp(self) -> None:
        self.clean_up()

    def tearDown(self) -> None:
        self.clean_up()

    def test_small(self):
        # Arrange
        input_string = """
            $
                function alert(message integer) 
                {
                    message1 = message + 1;
                    message2 = message + 2;
                    message3 = message + 3;
                }
                
                function alert(message integer) 
                {
                    if (len(message) > 0)
                    {
                        print(message);
                    }
                    endif
                }
            $
                [* Comments goes here *]
                real width, height;
                integer numOfSides;
                [* Comments goes here *]
                integer red, green, blue;

                [* Multiline comment goes here 
                    here here....
                    here.                
                *]
                boolean isSquare;                
            $ 
                [*This is a comment*]
                [* This is anther comment *]
                a= b + z;
            $
            """

        # Act 1: Create a test file
        write_to_file(self.SAMPLE_FILE_PATH, input_string)

        # Act 2 Run rat24s.py
        extract_tokens_command = f"python3 rat24s.py {self.SAMPLE_FILE_PATH} --tokens --output {self.LEXER_OUTPUT_PATH}"
        check_syntax_command = f"python3 rat24s.py {self.SAMPLE_FILE_PATH} --syntax --output {self.PARSER_OUTPUT_PATH}"

        run_command(extract_tokens_command)
        check_syntax_command_output = run_command(check_syntax_command)

        tokens_from_lexer = read_tokens_from_lexer_output(self.LEXER_OUTPUT_PATH)
        tokens_from_parser = read_tokens_from_parser_output(self.PARSER_OUTPUT_PATH)

        # Assert
        self.assertListEqual(tokens_from_lexer, tokens_from_parser)
        self.assertIn("Syntax is correct", check_syntax_command_output)

    def test_medium(self):
        # Arrange
        input_string = """
            $
                function alert(p1, p2 real, x, y, z boolean) 
                {
                    sum = p1 + p2;
                }

                function isPrime(n integer) {
                    prime = true;
                    i = 2;
                    while (i <= n) {
                        if (mod(n, i) == 0) 
                            prime = false;
                        else
                            i = i + 1;
                        endif                        
                    }
                    endwhile
                    return prime;
                }
            $
            
            $ 
                { a= b + z; } 
                while (d == true)
                {
                    a= b + z;
                    if (a > 0)
                        a = a / 2;
                    endif
                }
                endwhile
            $
            """

        # Act 1: Create a test file
        write_to_file(self.SAMPLE_FILE_PATH, input_string)

        # Act 2 Run rat24s.py
        extract_tokens_command = f"python3 rat24s.py {self.SAMPLE_FILE_PATH} --tokens --output {self.LEXER_OUTPUT_PATH}"
        check_syntax_command = f"python3 rat24s.py {self.SAMPLE_FILE_PATH} --syntax --output {self.PARSER_OUTPUT_PATH}"

        run_command(extract_tokens_command)
        check_syntax_command_output = run_command(check_syntax_command)

        tokens_from_lexer = read_tokens_from_lexer_output(self.LEXER_OUTPUT_PATH)
        tokens_from_parser = read_tokens_from_parser_output(self.PARSER_OUTPUT_PATH)

        # Assert
        self.assertListEqual(tokens_from_lexer, tokens_from_parser)
        self.assertIn("Syntax is correct", check_syntax_command_output)
    def test_large(self):
        # Arrange
        input_string = """
            $
                [*This is where the optional function definitions go*]
                function this_one(a integer, b boolean, c , d real) {
                    [*You can add Parameter Lists here, if you want*]
                    purple = a +c / d;
                    scan (a, b, c, d);
                    print (a);
                    
                    return purple;
                }

                function multi(p1, p2 real, x, y, z boolean) integer helper; {
                    sum = p1 + p2;
                    diff = sum - y;
                    multi = diff + sum + 30;
                    if (multi == x)
                        z = true;
                    else
                        z = false;
                    endif
                    return z;
                }

                function random(n integer) {
                
                    [* If n is less than 2, it's not prime *]
                    if (n < 2) 
                        return false;
                    endif

                    [*Check if 2 is a divisor (special case) *]
                    if (n == 2) 
                        return true;
                    endif

                    [* Check if n is even, hence not prime*]
                    if (mod(n, i) == 0) 
                        return false;
                    endif

                    [* Only need to check up to the square root of n *]
                    while (i * i <= n) {
                        [* If n is divisible by i, then n is not prime *]
                        if (mod(n, i) == 0) 
                            prime = false;
                            [* Exit loop if not prime*]
                        else
                            [* Increment by 2, skip even numbers*]
                            i = i + 2;
                        endif                        
                    }

                    [* End the loop*]
                    endwhile

                    return prime;
                }

            $
                [*This is where the optional declaration list goes*]
                integer trememdous;
                real fantastic;
                boolean maybetrue;
            $   
                [*This is where the statement list goes*]
                p =56;
                adding = 87;
                switch = false;
                bad_switch = true;
                print (this + that);
                scan (things, purple,strawberry);

                { a= b + z; 
                  helper = 87 + 68;
                  [*This is a list of compound statment lists*]
                } 
                while (d == true)
                {
                    a= b + z;
                    if (a > 0)
                        a = a / 2;
                    endif
                }
                endwhile
            $
            """

        # Act 1: Create a test file
        write_to_file(self.SAMPLE_FILE_PATH, input_string)

        # Act 2 Run rat24s.py
        extract_tokens_command = f"python3 rat24s.py {self.SAMPLE_FILE_PATH} --tokens --output {self.LEXER_OUTPUT_PATH}"
        check_syntax_command = f"python3 rat24s.py {self.SAMPLE_FILE_PATH} --syntax --output {self.PARSER_OUTPUT_PATH}"

        run_command(extract_tokens_command)
        check_syntax_command_output = run_command(check_syntax_command)

        tokens_from_lexer = read_tokens_from_lexer_output(self.LEXER_OUTPUT_PATH)
        tokens_from_parser = read_tokens_from_parser_output(self.PARSER_OUTPUT_PATH)

        # Assert
        self.assertListEqual(tokens_from_lexer, tokens_from_parser)
        self.assertIn("Syntax is correct", check_syntax_command_output)

if __name__ == '__main__':
    unittest.main()