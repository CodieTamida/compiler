from common.enums import TokenType, Operator
from components.lexcical_analyzer import Lexer, Token
from components.symbol_table import SymbolTable
from dataclasses import dataclass


class SemanticChecker:
    def __init__(self, symbol_table: SymbolTable):
        self.__symbol_table = symbol_table

    def determine_data_type(self, token: Token) -> TokenType:
        """
        Determines the data type of a given token.

        Parameters:
        - token (Token): The token whose data type needs to be determined.

        Returns:
        - TokenType: The data type of the token.
        """
        if token.token_type == TokenType.IDENTIFIER:
            symbol = self.__symbol_table.get(token.lexeme)
            return symbol.data_type
        else:
            return token.token_type

    def validate_arithmetic_operation(self, lhs: Token, rhs: Token):
        """
        Validates an arithmetic operation between two tokens.

        Parameters:
        - lhs (Token): The left-hand side token of the arithmetic operation.
        - rhs (Token): The right-hand side token of the arithmetic operation.

        Raises:
        - TypeError: If the operation involves booleans.
        """
        lsh_type = self.determine_data_type(lhs)
        rhs_type = self.determine_data_type(rhs)

        # Rule 1: No arithmetic operations are allowed for booleans
        if lsh_type == TokenType.BOOLEAN or rhs_type == TokenType.BOOLEAN:
            raise TypeError(
                "No arithmetic operations are allowed for booleans")
