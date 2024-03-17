def strlen(string: str) -> int:
    """
    Diye gaye string ki length return karo
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    count = 0
    for i in string:
        count += 1
    return count