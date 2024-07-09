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
    if len(l) + 1 == len(set(l)):
        l.sort()
        return False
    for i in range(1, len(l)):
        if l[i] < l[i - 1] and l[i] != l[i + 1]:
            return False
    return True