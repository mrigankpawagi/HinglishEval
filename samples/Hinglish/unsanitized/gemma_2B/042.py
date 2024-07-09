

def incr_list(l: list):
    """
    Elements ko 1 se badhakar wala list return karo.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]


def decr_list(l: list):
    """
    Elements ko 1 se badhakar wala list return karo.
    >>> decr_list([1, 2, 3])
    [1, 2, 3]
    >>> decr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [4, 2, 3, 1, 2, 2, 8, 1, 122]
    """
    return [x - 1 for x in l]


def add_list(l1: list, l2: list):
    """
    Elements ko 1 se badhakar wala list return karo.
    >>> add_list([1, 2, 3], [4, 5, 6])
    [5, 7, 9]
    >>> add_list([5, 3, 5, 2, 3, 3, 9, 0, 123], [4, 5, 6])
    [9, 8, 11, 7, 6, 9, 15, 1, 124]
    """
    return [x + y for x, y in zip(l1, l2)]


def sub_list(l1: list, l2: list):
    """
    Elements ko 1 se badhakar wala list return karo.
    >>> sub_list([1, 2, 3], [4, 5, 6])
    [3, 1, 3]
    >>> sub_list([5, 3, 5, 2, 3, 3, 9, 0, 123], [4, 5, 6])
    [1, 2, 1, 1, 1, 1, 1, 1, 1]
    """
    return [x - y for x, y in zip(l1, l2)]


def mul_list(l1: list, l2: list):
    """
    Elements ko 1 se