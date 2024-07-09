

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:
        raise EmptyTupleError
    a, b = 0, 1
    max_val = l[a]
    while  b <= len(l):
        if l[b] > max_val:
            max_val = l[b]
        b += 1
    return max_val









