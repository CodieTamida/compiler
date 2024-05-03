from io import StringIO
from typing import Optional
from dataclasses import dataclass


class InstructionTable:
    @dataclass
    class Instruction:
        address: int
        operation: str
        operand: str

    def __init__(self, initial_address=1):
        """
        Initializes a SymbolTable object with an initial memory address.

        Parameters:
        - initial_address (int, optional): The initial memory address. Defaults to 5000.
        """
        self.__entries = dict()
        self.__current_address = initial_address

    def generate_instruction(self, operation: str, operand: str) -> int:
        """
        Generates an intermediate code instruction and adds it to the instruction table.

        Parameters:
        - operation (str): The operation of the instruction.
        - operand (str): The operand of the instruction.

        Returns:
        - int: The address allocated to the instruction
        """
        e = self.Instruction(self.__current_address, operation, str(operand))
        self.__entries[self.__current_address] = e
        self.__current_address += 1
        return e.address

    def back_patch(self, instruction_address) -> int:
        raise NotImplementedError("This function hasn't been implemented yet.")

    def get_assembly_code(self) -> str:
        """
        Get the generated code.

        Returns:
        - str: The generated code as a string.
        """
        string_builder = StringIO()

        for e in self.__entries.values():
            if e.operand:
                string_builder.write(f"{e.operation} {e.operand}\n")
            else:
                string_builder.write(f"{e.operation}\n")

        return string_builder.getvalue()

    def print_table(self):
        """
        Prints the instruction table.
        """
        print("Instruction Table:")
        print(f"{'Address':<10}{'Operation':<15}{'Operand':<15}")
        print("-" * 40)
        for e in self.__entries.values():
            print(f"{e.address:<10}{e.operation:<15}{e.operand:<15}")
