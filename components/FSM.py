from dataclasses import dataclass
from common.enums import TokenType
from common.helpers import FileStream


@dataclass
class TraceResult:
    """
    Represents a token in a programming language lexer.

    Attributes:
        lexeme (str): The textual representation of the token.
        token_type (TokenType): The type of the token.
    """
    lexeme = str()
    paths = []
    final_states = []
    accepted_states = []
    accepted = False

    def __repr__(self):
        return f'TraceResult(accepted={self.accepted}, lexeme={self.lexeme}, paths={self.paths})'


class FSM:

    def __init__(self, sigma: list, states: list, initial_state: str, accepting_states: list, transition_table, char_to_symbol_mapping_func=None):
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
            raise ValueError(
                "Duplicate elements found in the AcceptingStates list.")

        self.sigma = sigma
        self.states = states
        self.initial_state = initial_state
        self.transition_table = transition_table
        self.accepting_states = accepting_states
        self.char_to_symbol_mapping_func = char_to_symbol_mapping_func

    def traceDFSM(self, first_char, filestream: FileStream, stop_signs: set) -> TraceResult:
        """
        Trace the Deterministic Finite State Machine (DFSM) with the given input stream 
        until encountering a stop sign or reaching the end of the file.

        Args:
            first_char (str): The first character to start tracing the DFSM.
            filestream (FileStream): The input stream to read characters from.
            stop_signs (set): A set of characters indicating where to stop tracing.

        Returns:
            TraceResult: An object containing information about the trace result, including the path taken by the DFSM, the lexeme read, final states reached, accepted states, and whether the input was accepted.
        """
        trace_result = TraceResult()

        current_state = self.initial_state
        path = [current_state]
        buffered_chars = []
        char = first_char

        # Loop until the end of the file
        while char and (char not in stop_signs):
            buffered_chars.append(char)

            row = self.states.index(current_state)
            if self.char_to_symbol_mapping_func:
                symbol = self.char_to_symbol_mapping_func(char)
            else:
                symbol = char

            if row >= 0 and symbol in self.sigma:
                col = self.sigma.index(symbol)
                current_state = self.transition_table[row][col]
                path.append(current_state)
            else:
                path.append("NULL")

            # Read the next character
            char = filestream.read(1)

        
        filestream.unread(char)

        trace_result.paths = [path]
        trace_result.lexeme = ''.join(buffered_chars)
        trace_result.final_states = path[-1]
        trace_result.accepted_states = list(set(trace_result.final_states) & set(self.accepting_states))
        trace_result.accepted = len(trace_result.accepted_states) > 0
        return trace_result
