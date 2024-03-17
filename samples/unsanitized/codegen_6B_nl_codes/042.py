

def incr_list(l: list):
    """
    Elements ko 1 se badhakar wala list return karo.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    def _incr_list(l, n):
        if n >= len(l):
            new_list = [l[0]] * (n + 1)
        else:
            new_list = [l[0]] + [l[n]] + _incr_list(l[n + 1:], len(l) - n - 1)
        return new_list
    return list(map(_incr_list, l, len(l)))

