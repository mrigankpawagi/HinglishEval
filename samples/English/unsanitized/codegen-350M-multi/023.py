

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    string = string.encode('utf-8')
    length = len(string)
    return length


