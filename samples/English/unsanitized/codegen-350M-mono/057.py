

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    a = l[0] < l[1] < l[2] < l[-2] < l[-1]
    if a: return False
    i = 0
    for el in l[3: ]:
        if el < l[1]-l[0]:
            return False
        i = 1 + i
    return True

