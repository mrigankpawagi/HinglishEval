

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
    [-1, -4]
    >>> get_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [-5, -3, -10]
    """
    return [x for x in l if x < 0]


def get_even(l: list):
    """
    List mein se sirf even numbers return karo.
    >>> get_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [2, 4, 6, 8, 10]
    >>> get_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    """
    return [x for x in l if x % 2 == 0]


def get_odd(l: list):
    """
    List mein se sirf odd numbers return karo.
    >>> get_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 3, 5, 7, 9]
    >>> get_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20