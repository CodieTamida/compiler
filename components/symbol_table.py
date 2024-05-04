from typing import Optional
from dataclasses import dataclass


class SymbolTable:
    @dataclass
    class Symbol:
        identifier: str
        address: int
        data_type: str

    def __init__(self, initial_address=5000):
        """
        Initializes a SymbolTable object with an initial memory address.

        Parameters:
        - initial_address (int, optional): The initial memory address. Defaults to 5000.
        """
        self.__entries = dict()
        self.__current_address = initial_address

    def add(self, identifier, data_type) -> int:
        """
        Adds an identifier to the symbol table.

        Parameters:
        - identifier (str): The identifier.
        - data_type (str): The data type.

        Returns:
        - int: The memory address allocated to the symbol.

        Raises:
        - NameError: If the identifier already exists in the symbol table.
        """
        if identifier in self.__entries:
            raise NameError(
                f"Variable '{identifier}' has already been declared.")

        symbol = SymbolTable.Symbol(
            identifier, self.__current_address, data_type)
        self.__entries[identifier] = symbol
        self.__current_address += 1
        return symbol.address

    def get(self, identifier) -> Optional[Symbol]:
        """
        Retrieves a symbol from the symbol table.

        Parameters:
        - identifier (str): The identifier of the symbol to retrieve.

        Returns:
        - Optional[Symbol]: The Symbol object if found, or None if the symbol is not in the table.
        """
        return self.__entries.get(identifier)

    def get_address(self, identifier) -> int:
        """
        Retrieves the memory address of an identifier from the symbol table.

        Parameters:
        - identifier (str): The identifier of the symbol.

        Returns:
        - int: The memory address of the symbol.

        Raises:
        - NameError: If the variable is not defined in the symbol table.
        """
        try:
            symbol = self.__entries.get(identifier)
            return symbol.address
        except:
            raise NameError(f"Variable '{identifier}' is not defined.")

    def print_table(self):
        """
        Prints the contents of the symbol table.
        """
        print("Symbol Table:")
        print(f"{'Identifier':<15}{'Address':<10}{'Type':<15}")
        print("-" * 40)
        for e in self.__entries.values():
            print(f"{e.identifier:<15}{e.address:<10}{e.data_type.name:<15}")
