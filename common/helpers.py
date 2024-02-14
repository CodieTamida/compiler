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
