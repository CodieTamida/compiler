from functions import *
from common.helpers import print_tokens
from components.lexcical_analyzer import tokenize


def main():
    word = "hello_wore3d"
    num = "00123g45"
    print(word)
    print(isIdentifier(word))
    print(isInteger(num))

    print("#############")

    # User input
    input_str = """
            while (fahr <= upper) 
            {
                a = 23.00;
                b = 9;
            }
        """
    
    # Tokenize
    tokens = tokenize(input_str)
    
    # Print to console
    print_tokens(tokens)

if __name__ == '__main__':
    main()
