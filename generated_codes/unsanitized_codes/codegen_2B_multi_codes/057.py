

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Compare first and second elements, return False for inequality.
    return all((a <= b) or (a >= b) for a, b in zip(l, l[1:]))


if __name__ == "__main__":
    # Unit test.
    import doctest
    doctest.testmod()
