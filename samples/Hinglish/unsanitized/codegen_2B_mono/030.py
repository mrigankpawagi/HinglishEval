

def get_positive(l: list):
    """
    List mein se sirf positive numbers return karo.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    out = []
    for i in l:
        if i > 0:
            out.append(i)
    return out

