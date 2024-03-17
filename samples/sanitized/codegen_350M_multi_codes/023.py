def strlen(string: str) -> int:
    """
    Diye gaye string ki length return karo
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    length = 0
    for ch in string:
        length += 1
    try:
        return length
    except TypeError as e:
        return len(str(ch))
    return 1