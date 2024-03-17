

def get_positive(l: list):
    """
    List mein se sirf positive numbers return karo.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [x for x in l if x > 0]


def get_negative(l: list):
    """
    List mein se sirf negative numbers return karo.
    >>> get_negative([-1, 2, -4, 5, 6])
    [-1, -4, -5, -6]
    >>> get_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-5, -3, -9, -10]
    """
    return [x for x in l if x < 0]


def get_positive_negative(l: list):
    """
    List mein se sirf positive and negative numbers return karo.
    >>> get_positive_negative([-1, 2, -4, 5, 6])
    [2, 5, 6, -1, -4, -5, -6]
    >>> get_positive_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1, -10, -5, -3, -9]
    """
    return get_positive(l) + get_negative(l)


def get_positive_negative_list(l: list):
    """
    List mein se sirf positive and negative numbers return karo.
    >>> get_positive_negative_list([-1, 2, -4, 5, 6])
    [2, 5, 6, -1, -4, -5, -6]
    >>> get_positive_negative_list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1, -10, -5, -3, -9]
    """
    return [x for x in l if x > 0] + [x for x