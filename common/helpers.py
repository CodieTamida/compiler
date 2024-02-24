from io import StringIO


def print_tokens(tokens: tuple):
    result = StringIO()

    # Write table headers
    result.write(f"{'token':<20} {'lexeme':<10}\n")
    result.write("-" * 31)

    # Write table rows
    for e in tokens:
        token_type, lexeme = e
        result.write(f"\n{token_type.name.lower():<20} {lexeme:<10}")

    # return result.getvalue()
    print(result.getvalue())

class FileStream:
    def __init__(self, file_path):
        self.file = open(file_path, 'r')
        self.buffer = list()

    def read(self, num_chars):
        buffered_chars = ''.join(self.buffer[:num_chars])
        del self.buffer[:num_chars]
        remaining_chars = num_chars - len(buffered_chars)
        file_chars = self.file.read(remaining_chars)
        return buffered_chars + file_chars

    def unread(self, char):
        self.buffer.insert(0, char)

    def close(self):
        self.file.close()
