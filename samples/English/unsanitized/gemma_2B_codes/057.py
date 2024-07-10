

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    i = 0
    if not l:
        return False
    if l[0] != l[-1]:
        return False
    if l[0] < l[-1]:
        return False

    while i < len(l) - 1:
        if (l[i] - l[i+1]) < 0:
            # Monotonically decreasing
            return False
        if (l[-1] - l[i]) < 0:
            # Monotonically increasing
            return False
        i += 1

    return True


def find_start(l: list):
    """Return the index of the first element in the list `l` that is negative.
    If the indices of the elements in the list are zero-based, return l[0].
    """
    for i in range(len(l)):
        if l[i] < 0:
            return i


def find_end(l: list):
    """Return the index of the last element in the list `l` that is negative.
    """
    i = len(l) - 1
    while i > 0:
        if l[i] < 0:
            return i
        i -= 1

    return 0
