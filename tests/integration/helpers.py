import subprocess

def write_to_file(filename, content):
    """
    Writes the given content to a file with the specified filename.

    Parameters:
    - filename (str): The name of the file to write to.
    - content (str): The content to be written to the file.
    """
    file = open(filename, 'w')
    file.write(content)
    file.close()

def run_command(command):
    """
    Execute the command capture its output
    """
    # Execute the command and capture its output
    output = subprocess.check_output(command, shell=True)

    # Decode the output from bytes to string (assuming UTF-8 encoding)
    decoded_output = output.decode("utf-8")

    return decoded_output

def read_tokens_from_lexer_output(filename):
    tokens = list()

    # Open the text file for reading
    with open(filename, 'r') as file:
        # Skip the first two lines (header and separator line)
        next(file)
        next(file)
        
        # Iterate over each line in the file
        for line in file:
            # Split the line into token and lexeme using whitespace as the delimiter            
            tokentype, lexeme = line.split()
            tokens.append((tokentype, lexeme))

    return tokens


def read_tokens_from_parser_output(filename):
    tokens = list()

    # Open the text file for reading
    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace and split the line into tokens
            elements = line.strip().split()

            # Check if the line has tokens and lexemes
            if len(elements) == 4 and elements[0] == 'Token:' and elements[2] == 'Lexeme:':
                tokentype = elements[1].strip().lower()  # Left-align the token for formatting
                lexeme = elements[3]
                tokens.append((tokentype, lexeme))

    return tokens

