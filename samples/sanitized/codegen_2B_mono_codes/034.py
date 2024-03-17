def unique(l: list):
    """
    Ek list mein sorted unique elements return karo
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    seen = []
    final = []
    for num in l:
        if num not in seen:
            seen.append(num)
            final.append(num)
    return final