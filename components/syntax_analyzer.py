from common.enums import TokenType
from components.lexcical_analyzer import Lexer, Token


class Parser:
    def __init__(self, lexer: Lexer, debug_print=False):
        """
        Initialize the Parser object.

        Parameters:
        - lexer (Lexer): The lexer object responsible for tokenizing input.
        - debug_print (bool): A flag indicating whether to print production rules for debugging purposes.
        """
        self.__lexer = lexer

        # The current token retrieved from the Lexer
        self.__current_token = None

        # A switch for printing production rule
        self.__debug_print = debug_print

    def debug_print(self, text=str()):
        if self.__debug_print:
            print(text)

    def debug_print_current_token(self):
        if self.__debug_print:
            tokentype = self.__current_token.token_type.name.capitalize()
            print(
                f"Token: {tokentype:<20} Lexeme: {self.__current_token.lexeme}")

    def __match(self, expected_lexeme: str):
        """
        Compares the current token's lexeme with the expected lexeme.

        If the lexemes match, then advance to the next token using the lexer.get_next_token() method. 

        Otherwise, raise a ValueError indicating that the expected lexeme was not found.

        Parameters:
            expected_lexeme (str): The expected lexeme to match against the current token's lexeme.

        Raises:
            ValueError: If the current token's lexeme does not match the expected character.

        Returns:
            None

        This method is used in a lexer/parser system to validate tokens against expected characters. If the current token's lexeme matches the expected character, the method advances to the next token. Otherwise, it raises a ValueError indicating the mismatch.
        """

        if self.__current_token.lexeme == expected_lexeme:
            self.__current_token = self.__lexer.get_next_token()
        else:
            raise ValueError(
                f'Expected {expected_lexeme}, found {self.__current_token.lexeme}')

    def parse(self):
        """
        Parses the input by tokenizing it with the lexer and applying grammar rules.

        Returns:
            bool: True if parsing is successful, False otherwise.
        """
        try:
            self.r1_Rat24S()  # Apply grammar rules
            self.debug_print_current_token()
            self.__match("$")  # Check if input ends with '$' symbol
            return True  # Parsing successful
        except Exception as err:
            print(err)
            return False  # Parsing failed

    def r1_Rat24S(self):
        """
        Applies the production rule 1:
        <Rat24S> -> $ 
                    <Opt Function Definitions> 
                    $ 
                    <Opt Declaration List> 
                    $ 
                    <Statement List> 
                    $
        """
        # Get the first token
        self.__current_token = self.__lexer.get_next_token()
        self.debug_print_current_token()

        # Check if the first token is '$' symbol
        self.__match("$")

        if self.__current_token.lexeme == "function":
            self.debug_print("<Rat24S> -> <Function Definitions>")
        elif (self.__current_token.lexeme == "integer"
              or self.__current_token.lexeme == "real"
              or self.__current_token.lexeme == "boolean"):
            self.debug_print("<Rat24S> -> <Opt Declaration List>")

        # Statement
        self.debug_print("<Rat24S> -> <Statement List>")
        self.debug_print_current_token()
        self.r14_statement_list()

    def r2_optional_function_definitions(self):
        raise NotImplementedError("Must implement this method!")

    def r3_function_definitions(self):
        raise NotImplementedError("Must implement this method!")

    def r4_function(self):
        raise NotImplementedError("Must implement this method!")

    def r5_optional_parameter_list(self):
        raise NotImplementedError("Must implement this method!")

    def r6_parameter_list(self):
        raise NotImplementedError("Must implement this method!")

    def r7_parameter(self):
        raise NotImplementedError("Must implement this method!")

    def r8_qualifier(self):
        raise NotImplementedError("Must implement this method!")

    def r9_body(self):
        raise NotImplementedError("Must implement this method!")

    def r10_optional_declaration_list(self):
        raise NotImplementedError("Must implement this method!")

    def r11_declaration_list(self):
        raise NotImplementedError("Must implement this method!")

    def r12_declaration(self):
        raise NotImplementedError("Must implement this method!")

    def r13_ids(self):
        raise NotImplementedError("Must implement this method!")

    def r14_statement_list(self):
        """
        Applies the production rule 14:
        <Statement List> -> <Statement> | 
                            <Statement> <Statement List>
        """
        # self.debug_print("<Statement List> -> <Statement>")
        self.r15_statement()

    def r15_statement(self):
        """
        Applies the production rule 15:
        <Statement> -> <Compound> | <Assign> | 
                        <If> | <Return> | 
                        <Print> | <Scan> | <While>
        """
        lexeme = self.__current_token.lexeme.lower()
        #  Check if the current token is an opening brace for a compound statement
        if lexeme == "{":
            self.r16_compound()
        # Check if the current token is an identifier for an assignment statement
        elif self.__current_token.token_type == TokenType.IDENTIFIER:
            self.debug_print("<Statement> -> <Assign>")
            self.__match(self.__current_token.lexeme)  # Move to the next token
            self.r17_assign()
        # Check if the current token is the "if" keyword for an if statement
        elif lexeme == "if":
            self.r18_if()
        elif lexeme == "return":
            self.r19_return()
        elif lexeme == "print":
            self.r20_print()
        elif lexeme == "scan":
            self.r21_scan()
        elif lexeme == "while":
            self.r22_while()
            
        #  Check if there are more statements to process 
        # (not reached the end of input)
        if self.__current_token.lexeme != "$":
            self.r14_statement_list()

    def r16_compound(self):
        raise NotImplementedError("Must implement this method!")

    def r17_assign(self):
        """
        Applies the production rule 17:
        <Assign> -> <Identifier> = <Expression> ;
        """
        self.debug_print("<Assign> -> <Identifier> = <Expression> ;")

        self.debug_print_current_token()

        if self.__current_token.lexeme == "=":
            self.__match(self.__current_token.lexeme)  # Move to the next token
            self.r25a_expression()

    def r18_if(self):
        raise NotImplementedError("Must implement this method!")

    def r19_return(self):
        raise NotImplementedError("Must implement this method!")

    def r20_print(self):
        raise NotImplementedError("Must implement this method!")

    def r21_scan(self):
        raise NotImplementedError("Must implement this method!")

    def r22_while(self):
        raise NotImplementedError("Must implement this method!")

    def r23_condition(self):
        raise NotImplementedError("Must implement this method!")

    def r24_relop(self):
        raise NotImplementedError("Must implement this method!")

    def r25a_expression(self):
        """
        Applies the production rule 25a: 
        E -> TE'

        Notes:
        E is <Expression>
        E' is <Expression Prime>
        T is <Term>
        """

        self.debug_print_current_token()
        self.debug_print("<Expression> -> <Term> <Expression Prime>")

        self.r26a_term()
        self.r25b_expression_prime()

    def r25b_expression_prime(self):
        """
        Applies the production rule 25b: 
        E' -> +TE' | -TE' | ε

        Notes:
        E' is <Expression Prime>
        T is <Term>
        """
        # Check for '+' or '-' case
        if self.__current_token.lexeme == "+" or self.__current_token.lexeme == "-":
            self.debug_print(
                f"<Expression Prime> -> {self.__current_token.lexeme} <Term> <Expression Prime>")
            self.__match(self.__current_token.lexeme)  # Move to the next token
            self.debug_print_current_token()
            self.r26a_term()
            self.r25b_expression_prime()
        # Handle Epsilon case
        else:
            self.__match(self.__current_token.lexeme)  # Move to the next token
            self.debug_print("<Expression Prime> -> ε")

    def r26a_term(self):
        """
        Applies the production rule 26a:
        T -> FT'

        Notes:
        F is <Factor>
        T is <Term>
        T' is <Term Prime>
        """
        self.debug_print("<Term> -> <Factor> <Term Prime>")

        self.r27_factor()
        self.r26b_term_prime()

    def r26b_term_prime(self):
        """
        Applies the production rule 26b:
        T' -> *FT' | /FT' | F

        Notes:
        F is <Factor>
        T is <Term>
        T' is <Term Prime>
        """

        # Print current token for debugging purposes
        self.debug_print_current_token()

        # Check for '*' or '/' case
        if self.__current_token.lexeme == "*" or self.__current_token.lexeme == "/":
            # Generate and print production rule text
            text = f"<Term Prime> -> {self.__current_token.lexeme} <Factor> <Term Prime>"
            self.debug_print(text)

            self.__match(self.__current_token.lexeme)  # Move to the next token
            self.debug_print_current_token()

            # Apply production rules for Factor and Term Prime recursively
            self.r27_factor()
            self.r26b_term_prime()
        # Handle Epsilon case
        else:
            self.debug_print("<Term Prime> -> ε")

    def r27_factor(self):
        """
        Applies the production rule 27:
        <Factor> -> - <Primary> | <Primary>
        """

        if self.__current_token.lexeme == "-":
            self.__match(self.__current_token.lexeme)  # Move to the next token
            primary = self.r28_primary()
            self.debug_print(f"<Factor> -> - {primary}")
        else:
            primary = self.r28_primary()
            self.debug_print(f"<Factor> -> {primary}")

    def r28_primary(self):
        """
        Applies the production rule 28:
        <Primary> -> <Identifier> | <Integer> | 
                    <Identifier> ( <IDs> ) | 
                    ( <Expression> ) |
                    <Real> | true | false

        Returns:
            str: The text representing the parsed primary token
        """
        text = ""

        # Check if the current token is an identifier, integer, or real number
        if (self.__current_token.token_type == TokenType.IDENTIFIER
                    or self.__current_token.token_type == TokenType.INTEGER
                    or self.__current_token.token_type == TokenType.REAL
                ):
            text = f"<{self.__current_token.token_type.name}>"
        # Check if the current token is "true" or "false"
        elif (self.__current_token.lexeme == "true" or self.__current_token.lexeme == "false"):
            text = self.__current_token.lexeme

        # Handle error: The current token does not match any expected types
        else:
            raise ValueError(
                f'Expected `ID, Number, (Expression), boolean`, but found {self.__current_token.token_type}')

        self.__match(self.__current_token.lexeme)  # Move to the next token
        return text
