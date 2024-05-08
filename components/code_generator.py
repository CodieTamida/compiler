from io import StringIO
from dataclasses import dataclass
from components.lexcical_analyzer import Lexer
from components.syntax_analyzer import Parser
from components.symbol_table import SymbolTable
from components.instruction_table import InstructionTable


class CodeGenerator:

    def __init__(self, lexer: Lexer, initial_memory_address=5000):
        """
        Initializes the Code Generator object.
        """
        self.__symbol_table = SymbolTable(initial_memory_address)
        self.__parser = Parser(lexer=lexer, debug_print=False)

    def generate_assembly_code(self) -> str:
        """
        Generate assembly code

        Returns:
        - str: The generated code as a string.
        """
        self.__parser.enable_code_generation(symbol_table=self.__symbol_table)
        instruction_table = self.__parser.parse()

        string_builder = StringIO()

        for e in instruction_table.get_instructions().values():
            if e.operand:
                string_builder.write(f"{e.operation} {e.operand}\n")
            else:
                string_builder.write(f"{e.operation}\n")

        return string_builder.getvalue()

    def print_symbol_table(self):
        """
        Prints the symbol table.
        """
        self.__symbol_table.print_table()

    def print_instruction_table(self):
        """
        Prints the instruction table.
        """
        table = self.__parser.get_instruction_table()
        table.print_table()
