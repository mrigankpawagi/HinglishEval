def monotonic(l: list):
    """
    True return karo agar list ke elements monotonically badh rahe ho ya ghat rahe ho.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if isinstance(l, list):
        return l
    n = len(l)
    k = 0
    while n > 0:
        if (n) < 0 or k < n:
            break
    if n < 0:
        return l
    return l[k:]