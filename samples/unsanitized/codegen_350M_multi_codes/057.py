

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
    if not isinstance(l, list):
        return False
    if not l == [1]:
        return True
    if isinstance(l, list):
        return monotonic(l)
    if l == [2]:
        return isinstance(l[1], int) and abs(l[1] - l[0]) < 1
    return monotonic(l[1:])


