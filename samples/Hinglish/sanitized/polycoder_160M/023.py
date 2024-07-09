

def strlen(string: str) -> int:
    """
    Diye gaye string ki length return karo
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return (string.count('"') +
            string.index('"')
            - string.count('"') if string.index('"') < 0 else 0

