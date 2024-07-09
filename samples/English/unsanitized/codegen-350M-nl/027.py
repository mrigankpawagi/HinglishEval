

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    with open('strings' if'strings' else'strings.txt', 'w') as f:
        f.write(string.encode("ABCDEFG"))   # ASCII
        f.close
    with open('strings' if'strings' else'strings.txt', 'r') as r:
        f.write(string.encode("HHLUX"))    # Unicode
        f.close


