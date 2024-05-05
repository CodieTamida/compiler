from enum import Enum


class TokenType(Enum):
    IDENTIFIER = 1
    KEYWORD = 2
    REAL = 3
    INTEGER = 4
    OPERATOR = 5
    SEPARATOR = 6
    UNKNOWN = 7
    BOOLEAN = 8
    # The BOOLEAN datatype is just for Assignment 3: Code Generation.
    # - It is used to determine the datatype of an identifier so that we can check the type match
    # - Because no arithmetic operations are allowed for booleans


class Operation(Enum):
    """
    Enumeration of colors.

    - PUSHI: Pushes an integer onto the top of the stack.
    - PUSHM: Pushes the value stored at memory location onto the top of the stack.
    - POPM: Pops the value from the top of the stack and stores it at memory location.
    - SOUT: Pops the value from the top of the stack and outputs it to the standard output.
    - SIN: Gets the value from the standard input and place in onto the top of the stack.
    - A: Pops the first 2 items from the stack and push the sum onto the top of the stack.
    - S: Pops the first 2 items from stack and push the difference onto the stack (2nd item-1st item).
    - M: Pops the first 2 items from stack and push the product onto the top of the stack.
    - D: Pops the first two items from stack and push the result onto the stack (Second item / First item and ignore the remainder).
    - GRT: Pops two items from the stack and pushes 1 onto the stack if second item is larger otherwise push 0.
    - LES: Pops two items from the stack and pushes 1 onto the stack if the second item is smaller than first item otherwise push 0.
    - EQU: Pops two items from the stack and pushes 1 onto the stack if they are equal otherwise push 0.
    - NEQ: Pops two items from the stack and pushes 1 onto the stack if they are not equal otherwise push 0.
    - GEQ: Pops two items from the stack and pushes 1 onto the stack if second item is larger or equal otherwise push 0.
    - LEQ: Pops two items from the stack and pushes 1 onto the stack if second item is less or equal otherwise push 0.
    - JUMP0: Pops the stack and if the value is 0 then jump to Instruction Location.
    - JUMP: Unconditionally jump to Instruction Location.
    - LABEL: Empty Instruction; Provides the Instruction Location to jump to.
    """
    PUSHI = "PUSHI"
    PUSHM = "PUSHM"
    POPM = "POPM"
    SOUT = "SOUT"
    SIN = "SIN"
    A = "A"  # Addition
    S = "S"  # Subtraction
    M = "M"  # Multiplication
    D = "D"  # Division
    GRT = "GRT"
    LES = "LES"
    EQU = "EQU"
    NEQ = "NEQ"
    GEQ = "GEQ"
    LEQ = "LEQ"
    JUMP0 = "JUMP0"
    JUMP = "JUMP"
    LABEL = "LABEL"
