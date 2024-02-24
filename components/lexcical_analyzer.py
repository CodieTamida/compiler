from common.enums import TokenType
from common.reserved_words_symbols import KEYWORDS, SEPARATORS, SIMPLE_OPERATORS, COMPOUND_OPERATORS, DECIMAL_SEPARATOR
from dataclasses import dataclass
from components.FSM import FSM
from common.helpers import FileStream

@dataclass
class Token:
    """
    Represents a token in a programming language lexer.

    Attributes:
        lexeme (str): The textual representation of the token.
        token_type (TokenType): The type of the token.
    """

    lexeme: str
    token_type: TokenType


class Lexer:
    def __init__(self, file_path):
        """
        Initializes an instance of the FileReader class with the content of the specified file.

        Parameters:
            file_path (str): The path to the file to be read.

        Raises:
            FileNotFoundError: If the specified file_path does not exist.
            IOError: If an error occurs while attempting to read the file.
        """
        # Create Finite State Machines for IntegerReal and Identifier
        self.int_real_FSM = self.__build_int_real_FSM()
        self.identifier_FSM = self.__build_identifier_FSM()

        # Stop signs
        self.stop_signs = self.__get_stop_signs()
        
        self.tokens = list()
        # Open the file in read mode
        self.filestream = FileStream(file_path)
        self.current_char = None

        buffer = str()

        try:
            # Read the first character
            char = self.filestream.read(1)


            # Loop until the end of file
            while char:
                done = False

                # ****************************************
                # ********** IGNORE WHITESPACES **********
                # ****************************************
                if char == ' ' or char == '\n':
                    done = True

                # ****************************************
                # *********** INT OR REAL Check **********
                # ****************************************
                elif char.isdigit() or char == DECIMAL_SEPARATOR:
                    # Call FSM
                    result = self.int_real_FSM.traceDFSM(char, self.filestream, self.stop_signs)

                    if result.accepted and result.accepted_states[0] == 'B':
                        self.tokens.append(Token(result.lexeme, TokenType.INTEGER))
                    elif result.accepted and result.accepted_states[0] == 'D':
                        self.tokens.append(Token(result.lexeme, TokenType.REAL))
                    else:
                        self.tokens.append(Token(result.lexeme, TokenType.UNKNOWN))

                    done = True

                # ****************************************
                # *********** IDENTIFIER CHECK ***********
                # ****************************************
                elif char.isalpha():
                    # Call FSM
                    result = self.identifier_FSM.traceDFSM(char, self.filestream, self.stop_signs)

                    if result.accepted and result.lexeme in KEYWORDS:
                        self.tokens.append(Token(result.lexeme, TokenType.KEYWORD))
                    elif result.accepted:
                        self.tokens.append(Token(result.lexeme, TokenType.IDENTIFIER))
                    else:
                        self.tokens.append(Token(result.lexeme, TokenType.UNKNOWN))

                    done = True

                # ****************************************
                # *********** SEPARATORS Check ***********
                # ****************************************
                elif char in SEPARATORS:
                    self.tokens.append(Token(char, TokenType.SEPARATOR))
                    done = True

                # ****************************************
                # ******* COMPOUND_OPERATORS Check *******
                # ****************************************
                if not done:
                    peek = self.filestream.read(1)
                    buffer = char + peek
                    if buffer in COMPOUND_OPERATORS:
                        self.tokens.append(Token(buffer, TokenType.OPERATOR))
                        done = True
                    else:
                        self.filestream.unread(peek)

                # ****************************************
                # ******** SIMPLE_OPERATORS Check ********
                # ****************************************
                if not done and char in SIMPLE_OPERATORS:
                    self.tokens.append(Token(char, TokenType.OPERATOR))
                    done = True

                if not done:
                    self.tokens.append(Token(char, TokenType.UNKNOWN))
                    done = True


                # Read the next character
                char = self.filestream.read(1)
        finally:
            # Close the file
            self.filestream.close()
        
    def __get_stop_signs(self):
        new_set = set()

        # Extract the first character of each separator
        new_set.update({item[0] for item in SEPARATORS})

        # Extract the first character of each operator
        new_set.update({item[0] for item in SIMPLE_OPERATORS})

        # Extract the first character of each operator
        new_set.update({item[0] for item in COMPOUND_OPERATORS})

        # Add a space character and newline character
        new_set.update({' ', '\n'})

        return new_set

    def __build_int_real_FSM(self):
        # FSM Configurations
        sigma = ['d', '.']
        states = ['A', 'B', 'C', 'D', 'E']
        initial_state = 'A'
        accepting_states = ['B', 'D']  # B: Integer, D: Real
        transition_table = [['B', 'E'],
                            ['B', 'C'],
                            ['D', 'E'],
                            ['D', 'E'],
                            ['E', 'E']]

        # Mapping function
        def char_to_symbol(char):
            if char.isdigit():
                return 'd'
            elif char.isalpha():
                return 'l'
            else:
                return char

        # Create an FSM instance
        fsm = FSM(sigma, states, initial_state,
                  accepting_states, transition_table, char_to_symbol)

        return fsm

    def __build_identifier_FSM(self):
        # FSM Configurations
        sigma = ['l', 'd', '_']
        states = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
        initial_state = 'A'
        accepting_states = ['B', 'D', 'E', 'F']
        transition_table = [['B', 'C', 'C'],
                            ['D', 'E', 'F'],
                            ['C', 'C', 'C'],
                            ['D', 'E', 'F'],
                            ['D', 'E', 'F'],
                            ['D', 'E', 'F'],
                            ['D', 'E', 'F'],
                            ['D', 'C', 'C'],
                            ['C', 'E', 'C'],
                            ['C', 'C', 'F'],
                            ['D', 'E', 'F'],
                            ['C', 'C', 'C']]

        # Mapping function
        def char_to_symbol(char):
            if char.isdigit():
                return 'd'
            elif char.isalpha():
                return 'l'
            else:
                return char

        # Create an FSM instance
        fsm = FSM(sigma, states, initial_state,
                  accepting_states, transition_table, char_to_symbol)

        return fsm


def tokenize(inputstring):
    raise NotImplementedError()
