

def incr_list(l: list):
    """
    Elements ko 1 se badhakar wala list return karo.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    if not l.is_keyed_by('ko1'):
        return False
    k1, k2, value = l.get(0, 1)
    if not value:
        return False
    l2k = k1
    if l2k in l.keys():
        return True
    else:
        k1 = k2
        rn = l.get(k1, 1)
        if not rn:
            return False
    return True
