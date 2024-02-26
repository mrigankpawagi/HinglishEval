

def strlen(string: str) -> int:
    """
    Diye gaye string ki length return karo
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    new_length = sum([ord(c) for c in string])
    return new_length // 2
