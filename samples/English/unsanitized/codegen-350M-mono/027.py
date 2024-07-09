

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return "".join([string[char].lower() if char.isupper() else char.upper()
                    for char in string])

########################################################################
# Problem 01

