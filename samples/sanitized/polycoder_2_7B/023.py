def strlen(string: str) -> int:
    """
    Diye gaye string ki length return karo
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    n = len(string)
    if n == 0:
        return 0
    return int(n)
