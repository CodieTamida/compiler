from common.enums import TokenType
from components.lexcical_analyzer import Lexer, Token


class Parser:
    def __init__(self, lexer: Lexer, debug_print=False):
        """
        Initializes the Parser object.

        Parameters:
        - lexer (Lexer): A Lexer object that generates tokens for parsing.
        - debug_print (bool): A flag indicating whether to print a text to the console for debugging purposes.
        """
        self.__lexer = lexer
        self.__current_token = None  # Used to store extracted token from the Lexer
        self.__debug_print = debug_print

    def debug_print(self, text=str()):
        """
        Print the provided text if debug_print flag is True.

        Parameters:
        - text (str): The text to be printed.
        """
        if self.__debug_print:
            print(text)

    def debug_print_current_token(self):
        """
        Prints information about the current token if debug_print flag is True
        """
        if self.__debug_print:
            tokentype = self.__current_token.token_type.name.capitalize()
            print(
                f"Token: {tokentype:<20} Lexeme: {self.__current_token.lexeme}")

    def parse(self):
        """
        Parses the input by tokenizing it with the lexer and applying grammar rules.

        Returns:
            bool: True if parsing is successful, False otherwise.
        """
        parsing_result = False  # Initialize parsing result to False

        try:
            # Get the first token
            self.__current_token = self.__lexer.get_next_token()
            if self.__current_token is None:
                raise ValueError(f"The input is empty")

            # Apply the entry point rule, <Rat24S>
            self.__r1_Rat24S()

            # Set parsing_result to True, indicating that the parsing process was successful
            #  and there are no more tokens to be processed.
            # Otherwise, raise a ValueError
            if self.__current_token is None:
                parsing_result = True  # Parsing successful
            else:
                self.debug_print_current_token()
                raise ValueError(
                    f"Expected End Of File, but found {self.__current_token.lexeme}")
        except Exception as err:
            red_color = "\033[91m"  # ANSI escape code for red color
            reset_color = "\033[0m"  # ANSI escape code to reset
            print(red_color + "Error:", err, reset_color)
        finally:
            return parsing_result

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
        """

        if self.__current_token.lexeme == expected_lexeme:
            self.__current_token = self.__lexer.get_next_token()
        else:
            raise ValueError(
                f'Expected {expected_lexeme}, found {self.__current_token.lexeme}')

    def __r1_Rat24S(self):
        """
        Applies the grammar rule 1:
        <Rat24S> -> $ 
                    <Opt Function Definitions> 
                    $ 
                    <Opt Declaration List> 
                    $ 
                    <Statement List> 
                    $
        """
        # Match the beginning of <Rat24S>, indicated by "$".
        self.debug_print_current_token()
        self.__match("$")

        # Apply rule 2 <Opt Function Definitions>
        self.debug_print("<Rat24S> -> <Opt Function Definitions>")
        self.__r2_optional_function_definitions()

        # Match the end of <Opt Function Definitions>, indicated by "$".
        self.debug_print_current_token()
        self.__match("$")

        # Apply rule 10 <Opt Declaration List>
        self.debug_print("<Rat24S> -> <Opt Declaration List>")
        self.__r10_optional_declaration_list()

        # Match the end of <Opt Function Definitions>, indicated by "$".
        self.debug_print_current_token()
        self.__match("$")

        # Apply rule 14 <Statement List>
        self.__r14_statement_list()

        # Match the end of <Rat24S>, indicated by "$".
        self.debug_print_current_token()
        self.__match("$")

    def __r2_optional_function_definitions(self):
        """
        Applies the grammar rule 2: 
        <Opt Function Definitions> -> <Function Definitions> | ε
        """
        if self.__current_token.lexeme == "function":
            self.debug_print(
                "<Opt Function Definitions> -> <Function Definitions>")
            self.__r3a_function_definitions()
        else:
            self.debug_print("<Opt Function Definitions> -> ε")

    def __r3a_function_definitions(self):
        """
        Applies the production rule 3a: 
        <Function Definitions> -> <Function> <Function Definitions Prime>
        """
        self.debug_print(
            "<Function Definitions> -> <Function> <Function Definitions Prime>")
        self.__r4_function()
        self.__r3b_function_definitions_prime()

    def __r3b_function_definitions_prime(self):
        """
        Applies the production rule 3b: 
        <Function Definitions Prime> -> <Function Definitions> | ε
        """
        if self.__current_token.lexeme == "function":
            self.debug_print(
                "<Function Definitions Prime> -> <Function Definitions>")
            self.__r4_function()
        else:
            self.debug_print("<Function Definitions Prime> -> ε")

    def __r4_function(self):
        """
        Applies the production rule 4: 
        <Function> ::= function <Identifier> ( <Opt Parameter List> ) 
                                <Opt Declaration List> <Body>
        """
        self.debug_print_current_token()

        # Match the beginning of <Function>, indicated by "function".
        self.__match("function")  # Match and Move to the next token

        # Check if function's name exists
        if self.__current_token.token_type == TokenType.IDENTIFIER:
            self.debug_print(
                "<Function> -> function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>")
            self.debug_print_current_token()
            self.__match(self.__current_token.lexeme)  # Move to the next token

            # After the function's name, there must be an open parenthesis '('
            self.debug_print_current_token()
            self.__match("(")
            self.__r5_optional_parameter_list()

            # After the function's params, there must be a close parenthesis ')'
            self.debug_print_current_token()
            self.__match(")")

            self.__r10_optional_declaration_list()
            self.__r9_body()
        # Handle error: Function's name does not exist
        else:
            raise ValueError(
                f"Expected an Identifier, but found {self.__current_token.token_type}")

    def __r5_optional_parameter_list(self):
        """
        Applies the grammar rule 5: 
        <Opt Parameter List> -> <Parameter List> | ε
        """
        if self.__current_token.token_type == TokenType.IDENTIFIER:
            self.debug_print("<Opt Parameter List> -> <Parameter List>")
            self.__r6_parameter_list()
        else:
            self.debug_print("<Opt Parameter List> -> ε")

    def __r6_parameter_list(self):
        """
        Applies production rule r6
        <PL> -> <P> <P'>

        Notes:
        PL = <Parameter List>
        P  = <Parameter>
        P' = <Parameter Prime> 
        """
        self.debug_print_current_token()
        self.debug_print("<Parameter List> -> <Parameter> <Parameter Prime> ")
        self.__r7_parameter()
        self.__r6b_parameter_prime()
        
        #raise NotImplementedError("Must implement this method!")
    def __r6b_parameter_prime(self):
        """
        Applies production rule r6b
        <P'> -> ,<PL> | ε

        P' = Parameter Prime
        PL = Parameter List
        ε  = Epsilon
        """
        if self.__current_token.lexeme == ",":
            self.debug_print(f"<Parameter Prime> -> {self.__current_token.lexeme} <Parameter List>")
            self.__match(self.__current_token.lexeme)
            self.debug_print_current_token
            self.__r6_parameter_list()
        else:
            self.debug_print("<Parameter Prime> -> ε")


    def __r7_parameter(self):
        self.debug_print("<Parameter> -> <IDs> <Qualifier>")
        self.__r13_ids()
        self.__r8_qualifier()
        #raise NotImplementedError("Must implement this method!")

    def __r8_qualifier(self):
        if (self.__current_token.lexeme == "integer" or self.__current_token.lexeme == "boolean"  or 
        self.__current_token.lexeme == "real"):
            self.debug_print("<Qualifier> -> integer | boolean | real")
            self.__match(self.__current_token.lexeme)
            
        #raise NotImplementedError("Must implement this method!")

    def __r9_body(self):
        self.debug_print("<Body> -> { <Statement List> }")
        self.__match('{')
        self.__r14_statement_list()
        self.__match('}')

    def __r10_optional_declaration_list(self):
        if (self.__current_token.lexeme == "integer"
            or self.__current_token.lexeme == "real"
                or self.__current_token.lexeme == "boolean"):
            self.debug_print("<Opt Declaration List> -> <Declaration List>")
            self.__r11_declaration_list()
        else:
            self.debug_print("<Opt Declaration List> -> ε")

    def __r11_declaration_list(self):
        """
        Applies the production rule 11: 
        <Declaration List> -> <Declaration> ; <Declaration List Prime>
        """
        if (self.__current_token.lexeme == "integer"
            or self.__current_token.lexeme == "real"
                or self.__current_token.lexeme == "boolean"):            
            self.debug_print("<Declaration List> -> <Declaration> ;")
            self.__r12_declaration()
            self.debug_print_current_token()
            self.__match(";")
            self.__r11b_declaration_list_prime()

    def __r11b_declaration_list_prime(self):
        """
        Applies the production rule 11: 
        <Declaration List Prime> -> <Declaration List> | ε
        """
        if (self.__current_token.lexeme == "integer"
            or self.__current_token.lexeme == "real"
                or self.__current_token.lexeme == "boolean"):
            self.debug_print("<Declaration List Prime> -> <Declaration>")
            self.__r11_declaration_list()
        else:
            self.debug_print("<Declaration List Prime> -> ε")

    def __r12_declaration(self):
        """
        Applies the grammar rule 12: 
        <Declaration> ::= <Qualifier > <IDs>
        """
        self.debug_print_current_token()
        self.__r8_qualifier()
        self.__r13_ids()

    def __r13_ids(self):
        """
        Applies the production rule 13a: 
        <IDs> -> <Identifier> <IDs Prime>
        """
        self.debug_print_current_token()
        if self.__current_token.token_type == TokenType.IDENTIFIER:
            self.debug_print("<IDs> -> <Identifier> <IDs Prime>")
            self.__match(self.__current_token.lexeme)
            self.__r13b_ids_prime()
        else:
            raise ValueError(
                f"Expected an Identifier, but found {self.__current_token.token_type}")

    def __r13b_ids_prime(self):
        """
        Applies the production rule 13b: 
        <IDs Prime> -> , <IDs> | ε
        """
        if self.__current_token.lexeme == ",":
            self.debug_print("<IDs Prime> -> , <IDs>")
            self.__match(self.__current_token.lexeme)  # Move to the next token
            self.__r13_ids()
        else:
            self.debug_print("<IDs Prime> -> ε")

    def __r14_statement_list(self):
        """
        Applies the grammar rule 14:
        <Statement List> -> <Statement> | 
                            <Statement> <Statement List>
        """
        self.debug_print(
            "<Statement List> -> <Statement> | <Statement> <Statement List>")
        # self.debug_print_current_token()
        self.__r15_statement()

        #  Check if there are more statements to process
        if self.__current_token.lexeme != "}" and self.__current_token.lexeme != "$":
            self.__r14_statement_list()

    def __r15_statement(self):
        """
        Applies the grammar rule 15:
        <Statement> -> <Compound> | <Assign> | 
                        <If> | <Return> | 
                        <Print> | <Scan> | <While>
        """
        lexeme = self.__current_token.lexeme.lower()
        #  Check if the current token is an opening brace for a compound statement
        if lexeme == "{":
            self.__r16_compound()
        # Check if the current token is an identifier for an assignment statement
        elif self.__current_token.token_type == TokenType.IDENTIFIER:
            self.debug_print("<Statement> -> <Assign>")
            self.__match(self.__current_token.lexeme)  # Move to the next token
            self.__r17_assign()
        # Check if the current token is the "if" keyword for an if statement
        elif lexeme == "if":
            self.__r18_if()
        elif lexeme == "return":
            self.__r19_return()
        elif lexeme == "print":
            self.__r20_print()
        elif lexeme == "scan":
            self.__r21_scan()
        elif lexeme == "while":
            self.__r22_while()

    def __r16_compound(self):
        self.debug_print("<Compound> -> { <Statement List> }")
        self.__match('{')
        self.__r14_statement_list()
        self.__match('}')

    def __r17_assign(self):
        """
        Applies the grammar rule 17:
        <Assign> -> <Identifier> = <Expression> ;
        """
        self.debug_print("<Assign> -> <Identifier> = <Expression> ;")

        self.debug_print_current_token()

        if self.__current_token.lexeme == "=":
            self.__match(self.__current_token.lexeme)  # Move to the next token
            self.__r25a_expression()

            # Match the end of <Assign>, indicated by a semicolon ";".
            self.__match(";")  # Match & Move to the next token

    def __r18_if(self):
        raise NotImplementedError("Must implement this method!")

    def __r19_return(self):
        """
        Applies the production rule 19a:
        R --> rR'

        R = <Return>
        r = return
        R` = <Return Prime>
        """

        if self.__current_token.lexeme == "return":
            self.debug_print_current_token()
            expression = f'<Return> -> return <Return Prime>'
            self.debug_print(expression)

            self.__match(self.__current_token.lexeme)

            self.__r19_return_b_prime()
        else:
            self.debug_print(f"Expecting return keyword, but read {self.__current_token.lexeme}")

    def __r19_return_b_prime(self):
        """
        R' --> ; | E

        R' = <Return Prime>
        ; = symbol ;
        E = <Expression>
        """

        # Check to see if the current token is a separator, ;
        if self.__current_token.lexeme == ";":
            self.debug_print(f"<Return Prime> -> ;")
            self.__match(self.__current_token.lexeme) # Move to the next token

        
        # Check to see if <Expression>, after left-recursion, leads E -> TE'

        else:
            self.debug_print(f"<Return Prime> -> <Expression>;")
            self.__r25a_expression()
            self.__match(';')
        

    def __r20_print(self):
        self.__match("print")
        self.__match('(')
        self.__r25a_expression()
        self.debug_print_current_token()
        self.__match(')')
        self.__match(';')


    def __r21_scan(self):
        raise NotImplementedError("Must implement this method!")

    def __r22_while(self):
        raise NotImplementedError("Must implement this method!")

    def __r23_condition(self):
        raise NotImplementedError("Must implement this method!")

    def __r24_relop(self):
        raise NotImplementedError("Must implement this method!")

    def __r25a_expression(self):
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

        self.__r26a_term()
        self.__r25b_expression_prime()

    def __r25b_expression_prime(self):
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
            self.__r26a_term()
            self.__r25b_expression_prime()
        # Handle Epsilon case
        else:
            self.debug_print("<Expression Prime> -> ε")

    def __r26a_term(self):
        """
        Applies the production rule 26a:
        T -> FT'

        Notes:
        F is <Factor>
        T is <Term>
        T' is <Term Prime>
        """
        self.debug_print("<Term> -> <Factor> <Term Prime>")

        self.__r27_factor()
        self.__r26b_term_prime()

    def __r26b_term_prime(self):
        """
        Applies the production rule 26b:
        T' -> *FT' | /FT' | ε

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
            self.__r27_factor()
            self.__r26b_term_prime()
        # Handle Epsilon case
        else:
            self.debug_print("<Term Prime> -> ε")

    def __r27_factor(self):
        """
        Applies the grammar rule 27:
        <Factor> -> - <Primary> | <Primary>
        """
        text_to_print = ""

        if self.__current_token.lexeme == "-":
            self.__match(self.__current_token.lexeme)  # Move to the next token
            text_to_print = "<Factor> -> - "            
        else:
            text_to_print = "<Factor> -> "
        
        primary_type = self.__r28_primary()      

        if primary_type:
            text_to_print = f"{text_to_print} {primary_type}"
            self.debug_print(text_to_print)

    def __r28_primary(self):
        """
        Applies the grammar rule 28:
        <Primary> -> <Identifier> <Primary Prime> | 
                    <Integer> | ( <Expression> ) |
                    <Real> | true | false

        Returns:
            str: The text representing the parsed primary token
        """
        text = ""

        # Case 1: IDENTIFIER
        if self.__current_token.token_type == TokenType.IDENTIFIER:
            self.__match(self.__current_token.lexeme)  # Move to the next token
            text = self.__r28b_primary_prime()
            text = f"<Identifier> {text}"
        # Case 2: INTEGER, REAL
        elif (self.__current_token.token_type == TokenType.INTEGER
                or self.__current_token.token_type == TokenType.REAL
            ):
            text = f"<{self.__current_token.token_type.name}>"
            self.__match(self.__current_token.lexeme)  # Move to the next token
        # Case 3: "true" or "false"
        elif (self.__current_token.lexeme == "true" or self.__current_token.lexeme == "false"):
            text = self.__current_token.lexeme
            self.__match(self.__current_token.lexeme)  # Move to the next token
        # Case 4: ( <Expression> )
        elif self.__current_token.lexeme == "(":
            self.debug_print("<Primary Prime> -> ( <Expression> )")
            self.__match(self.__current_token.lexeme)  # Move to the next token
            self.__r25a_expression()
            self.__match(")")  # Match and Move to the next token
            self.debug_print("<Primary Prime> -> ( <Expression> )")
        # Handle error: The current token does not match any expected types
        else:
            raise ValueError(
                f'Expected `ID, Number, (Expression), boolean`, but found {self.__current_token.token_type}')

        return text

    def __r28b_primary_prime(self):
        """
        Applies the grammar rule 28:
        <Primary Prime> -> ( <IDs> ) | ε
        """
        text = ""
        if (self.__current_token.lexeme == "("):
            # After the function's name, there must be an open parenthesis '('
            self.debug_print_current_token()
            self.__match("(")  # Match and Move to the next token

            self.__r13_ids()

            # After the function's params, there must be a close parenthesis ')'
            self.debug_print_current_token()
            self.__match(")")  # Match and Move to the next token
            text = "( <IDs> )"
        # Handle Epsilon case
        else:
            self.debug_print("<Primary Prime> -> ε")

        return text
