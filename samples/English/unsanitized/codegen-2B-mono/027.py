

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return " ".join(filter(lambda c: c.isupper(), string)) + " " + " ".join(filter(lambda c: not c.isupper(), string))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
