import unittest
import os
from common.enums import TokenType
from components.lexcical_analyzer import FSM


class FSMTestCase(unittest.TestCase):

    def test_init(self):
        # Arrange
        sigma = ['d', '.']
        states = ['A', 'B', 'C', 'D', 'E']
        initial_states = ['A']
        accepting_states = ['D']
        transition_table = [[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]
        actual = None
        expected = True

        # Act
        try:
            fsm = FSM(sigma, states, initial_states,
                      accepting_states, transition_table)
            actual = True
        except:
            actual = False

        # Assert
        self.assertEqual(actual, expected)

    def test_init_with_duplicated_states(self):
        # Arrange
        sigma = ['d', '.']
        states = ['A', 'B', 'C', 'D', 'E', 'E']
        initial_states = ['A']
        accepting_states = ['D']
        transition_table = [[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]
        actual = None
        expected = False

        # Act
        try:
            fsm = FSM(sigma, states, initial_states,
                      accepting_states, transition_table)
        except:
            actual = False

        # Assert
        self.assertEqual(actual, expected)

    def test_traceDFSM_path(self):
        # Arrange
        sigma = ['d', '.']
        states = ['A', 'B', 'C', 'D', 'E']
        initial_state = 'A'
        accepting_states = ['D']
        transition_table = [['B', 'E'],
                            ['B', 'C'],
                            ['D', 'E'],
                            ['D', 'E'],
                            ['E', 'E']]
        input_string = "ddd.d"
        actual_path = None
        expected_path = ['A', 'B', 'B', 'B', 'C', 'D']

        # Act
        fsm = FSM(sigma, states, initial_state,
                  accepting_states, transition_table)
        actual_path = fsm.traceDFSM(input_string)

        # Assert
        self.assertEqual(actual_path, expected_path)

    def test_traceDFSM_accepted(self):
        # Arrange
        sigma = ['d', '.']
        states = ['A', 'B', 'C', 'D', 'E']
        initial_state = 'A'
        accepting_states = ['D']
        transition_table = [['B', 'E'],
                            ['B', 'C'],
                            ['D', 'E'],
                            ['D', 'E'],
                            ['E', 'E']]
        input_string = "ddd.d"
        actual_path = None
        expected_path = True

        # Act
        fsm = FSM(sigma, states, initial_state,
                  accepting_states, transition_table)
        actual_path = fsm.validate(input_string)

        # Assert
        self.assertEqual(actual_path, expected_path)

    def test_traceDFSM_rejected(self):
        # Arrange
        sigma = ['d', '.']
        states = ['A', 'B', 'C', 'D', 'E']
        initial_state = 'A'
        accepting_states = ['D']
        transition_table = [['B', 'E'],
                            ['B', 'C'],
                            ['D', 'E'],
                            ['D', 'E'],
                            ['E', 'E']]
        input_string = ".d"
        actual_path = None
        expected_path = False

        # Act
        fsm = FSM(sigma, states, initial_state,
                  accepting_states, transition_table)
        actual_path = fsm.validate(input_string)

        # Assert
        self.assertEqual(actual_path, expected_path)

    def test_traceDFSM_invalid_input(self):
        # Arrange
        sigma = ['d', '.']
        states = ['A', 'B', 'C', 'D', 'E']
        initial_state = 'A'
        accepting_states = ['D']
        transition_table = [['B', 'E'],
                            ['B', 'C'],
                            ['D', 'E'],
                            ['D', 'E'],
                            ['E', 'E']]
        input_string = "$#"
        actual_path = None
        expected_path = ['A']

        # Act
        fsm = FSM(sigma, states, initial_state,
                  accepting_states, transition_table)
        actual_path = fsm.traceDFSM(input_string)

        # Assert
        self.assertEqual(actual_path, expected_path)

    def test_traceDFSM_invalid_integer(self):
        # Arrange
        sigma = ['d']
        states = ['A', 'B']
        initial_state = 'A'
        accepting_states = ['B']
        transition_table = [['B'],
                            ['B']]
        input_string = ".d"
        actual = None
        expected = False

        # Act
        fsm = FSM(sigma, states, initial_state,
                  accepting_states, transition_table)
        actual = fsm.validate(input_string)

        # Assert
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
