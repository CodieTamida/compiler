from functions import *
from common.helpers import print_tokens
from components.lexcical_analyzer import Lexer


def main():
    KEYWORDS = {'function', 'integer','boolean', 'real', 'if' 'endif', 'else', 'return', 'print',
                'scan','while', 'endwhile', 'true', 'false'}
    SEPARATORS= {'$', '(', ')', ',', '{', '}'}
    OPERATORS = {'==', '!=', '>', '<', '<=', '=>', '*', '/'}
    
    word = "hello_wore3d"
    num = "00123g45"
    print(word)
    print(isIdentifier(word))
    print(isInteger(num))

    print("#############")

    lexer = Lexer("test_case_1.txt")
    
    while lexer.has_token():
        token = lexer.next_token()
        print(f"{token.token_type.name.lower():<20} {token.lexeme:<10}")

if __name__ == '__main__':
    main()
