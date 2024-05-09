from typing import Optional
from dataclasses import dataclass
from common.enums import Operator


class InstructionTable:
    @dataclass
    class Instruction:
        address: int  # Address of the instruction
        operation: str  # Operator code
        operand: Optional[str] = None  # Operand of the instruction, optional

    def __init__(self, initial_address=1):
        """
        Initializes a SymbolTable object with an initial memory address.

        Parameters:
        - initial_address (int, optional): The initial memory address. Defaults to 5000.
        """
        self.__entries = dict()
        self.__current_address = initial_address
        self.__jump_stack = list()

    def get_instructions(self) -> dict[int, Instruction]:
        return self.__entries

    def generate_instruction(self, operation: Operator, operand: str = None) -> int:
        """
        Generates an instruction with the given operation and operand.

        Parameters:
        - operation (Operator): The operation enum.
        - operand (str, optional): The operand of the instruction. Defaults to None.

        Returns:
        - int: The address of the generated instruction.
        """
        if operand != None:
            operand = str(operand)
        e = self.Instruction(self.__current_address, operation.value, operand)
        self.__entries[self.__current_address] = e
        self.__current_address += 1
        return e.address

    def push_jump_stack(self, instruction_address):
        self.__jump_stack.append(instruction_address)

    def pop_jump_stack(self):
        return self.__jump_stack.pop()
    
    def back_patch(self, instruction_address) -> int:
        """
        Back-patches an instruction.

        Parameters:
        - instruction_address: The address of the instruction to back-patch.

        Returns:
        - int: The address of the back-patched instruction.
        """
        address = self.pop_jump_stack()
        self.__entries.get(address).operand = instruction_address
        return address
    

    def print_table(self):
        """
        Prints the instruction table.
        """
        print("Instruction Table:")
        print(f"{'Address':<10}{'Operator':<15}{'Operand':<15}")
        print("-" * 40)
        for e in self.__entries.values():
            formatted_operand = e.operand if e.operand else 'nil'
            print(f"{e.address:<10}{e.operation:<15}{formatted_operand:<15}")
