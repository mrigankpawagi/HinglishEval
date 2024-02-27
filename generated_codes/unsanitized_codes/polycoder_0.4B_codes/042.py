

def incr_list(l: list):
    """
    Elements ko 1 se badhakar wala list return karo.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    if len(l) == 0:
        return []

    l = copy.copy(l)

    # wala muk list element wanleh lal wanya
    for i in range(len(l)):
        if i not in list:
            l[i] = [l[i], None]

    return l
