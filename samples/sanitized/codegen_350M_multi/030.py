def get_positive(l: list):
    """
    List mein se sirf positive numbers return karo.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    output = []
    for x in l:
        if x == -1 or x == 2:
            output.append(-x)
        elif x == -4 or x == 3 or x == 5 or x == 6:
            output.append(x)
        else:
            output.append(x)
    return output