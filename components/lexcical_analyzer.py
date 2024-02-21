from common.enums import TokenType
from common.reserved_words_symbols import KEYWORDS, SEPARATORS, SIMPLE_OPERATORS, COMPOUND_OPERATORS, OPERATORS
from dataclasses import dataclass
import re


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
        self.content = ""
        self.current_pos = 0
        self.file_length = 0
        self.stop_signs = self.__get_stop_signs()

        try:
            with open(file_path, 'r') as file:
                self.content = file.read()
                self.file_length = len(self.content)
        except Exception as e:
            raise e

    def eof(self):
        """
        Checks whether the current position in the file has reached End of File.

        Returns:
            bool: True if the current position is at End of File, False otherwise.
        """
        return self.current_pos >= self.file_length

    def has_token(self):
        end_pos = self.__next_start_index()
        return end_pos < self.file_length

    def next_token(self):
        """
        Retrieves the next token from the content.

        Returns:
            str or Token: The next token extracted from the content.
                        If the end of the content is reached, returns a Token object with type 'EOF' and value None.
        """
        token_type = TokenType.UNKNOWN

        # Update the current position to the next start index
        self.current_pos = self.__next_start_index()

        # Check if the current position is beyond the end of the content
        if self.current_pos >= self.file_length:
            raise EOFError("End of file reached.")

        # ****************************************
        # *********** SEPARATORS Check ***********
        # ****************************************
        elif self.content[self.current_pos] in SEPARATORS:
            end_pos = self.current_pos + 1
            token_type = TokenType.SEPARATOR

        # ****************************************
        # ******* COMPOUND_OPERATORS Check *******
        # ****************************************
        elif self.content.startswith(tuple(COMPOUND_OPERATORS), self.current_pos):
            end_pos = self.current_pos + 2
            token_type = TokenType.OPERATOR

        # ****************************************
        # ******** SIMPLE_OPERATORS Check ********
        # ****************************************
        elif self.content[self.current_pos] in SIMPLE_OPERATORS:
            end_pos = self.current_pos + 1
            token_type = TokenType.OPERATOR

        else:
            # Determine the end position of the next token
            end_pos = self.__next_stop_index()

        # Extract the next token from the content
        lexeme = self.content[self.current_pos:end_pos]

        # Update the current position to the end position of the token
        self.current_pos = end_pos

        # ****************************************
        # ************ KEYWORDS Check ************
        # ****************************************
        if lexeme in KEYWORDS:
            token_type = TokenType.KEYWORD

        ########################################################
        # Pass the lexeme to Integer, Real, and Identifier FSM #
        ########################################################

        return Token(lexeme, token_type)  # Return the extracted token

    def __next_start_index(self):
        i = self.current_pos
        while i < self.file_length and (self.content[i] == ' ' or self.content[i] == '\n'):
            i += 1
        return i

    def __next_stop_index(self):
        i = self.current_pos

        while i < self.file_length and self.content[i] not in self.stop_signs:
            i += 1

        return i

    def __get_stop_signs(self):
        new_set = set()

        # Extract the first character of each separator
        new_set.update({item[0] for item in SEPARATORS})

        # Extract the first character of each operator
        new_set.update({item[0] for item in OPERATORS})

        # Add a space character and newline character
        new_set.update({' ', '\n'})

        return new_set


class FSM:
    def __init__(self, sigma: list, states: list, initial_state: str, accepting_states: list, transition_table):
        """
        Initializes a Finite State Machine (FSM) object with the given parameters.

        Parameters:
        - sigma (list): The alphabet (input symbols) of the FSM.
        - states (list): The set of states in the FSM.
        - initial_states (list): The initial state(s) of the FSM.
        - transition_table (dict): The transition table of the FSM. 
        - accepting_states (list): The set of accepting states in the FSM.
        """
        if len(sigma) != len(set(sigma)):
            raise ValueError("Duplicate elements found in the Sigma list.")
        
        if len(states) != len(set(states)):
            raise ValueError("Duplicate elements found in the States list.")
        
        if len(accepting_states) != len(set(accepting_states)):
            raise ValueError("Duplicate elements found in the AcceptingStates list.")

        self.sigma = sigma
        self.states = states
        self.initial_state = initial_state
        self.transition_table = transition_table
        self.accepting_states = accepting_states

    def traceDFSM(self, input_string):
        """
        Traces the input string through the FSM and returns the final state reached.

        Parameters:
        - input_string (str): The input string to be traced through the FSM.

        Returns:
        - list: The list of final states reached after tracing the input string through the FSM.
        """
        current_state = self.initial_state
        path = [current_state]
        
        try:
            for char in input_string:
                row = self.states.index(current_state)
                col = self.sigma.index(char)
                current_state = self.transition_table[row][col]
                path.append(current_state)
        except Exception as e:
            print(e)
            path.append("NULL")

        return path

    def validate(self, input_string):
        """
        Checks if the input string is accepted by the FSM.

        Parameters:
        - input_string (str): The input string to be checked for acceptance.

        Returns:
        - bool: True if the input string is accepted by the FSM, False otherwise.
        """

        path = self.traceDFSM(input_string)
        return path[-1] in self.accepting_states

def tokenize(inputstring):
    raise NotImplementedError()