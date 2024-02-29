

def incr_list(l: list):
    """
    Elements ko 1 se badhakar wala list return karo.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    for i in range(len(l)):
        l[i] += 1
    return l


def incr_list_2(l: list):
    """
    Elements ko 1 se badhakar wala list return karo.
    >>> incr_list_2([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_2([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]


def incr_list_3(l: list):
    """
    Elements ko 1 se badhakar wala list return karo.
    >>> incr_list_3([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_3([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return list(map(lambda x: x + 1, l))


def incr_list_4(l: list):
    """
    Elements ko 1 se badhakar wala list return karo.
    >>> incr_list_4([1, 2, 3])
    [2, 3, 4]
    >>> incr_list_4([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]


def incr_list_5(l: list):
    """
    Elements ko 1 se badhakar wala list return karo.
    >>> incr_list_5([1, 2, 3])
    [2, 3,