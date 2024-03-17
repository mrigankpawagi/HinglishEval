

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
    if len(l) < 2:
        return True
    if l[0] < l[1]:
        return True
    return False
