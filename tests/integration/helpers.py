import os


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
