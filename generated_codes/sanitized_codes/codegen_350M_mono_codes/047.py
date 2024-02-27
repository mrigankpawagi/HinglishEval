def median(l: list):
    """
    List l ke elements ka median return karo.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    l = list(l)
    q_len = len(l) / 2
    q = l[int(q_len)]
    middle = l[int(q_len) - 1]
    if len(l) % 2 != 0:
        if q == None:
            return l[q_len]
        return (l[int(q_len) - 2] + l[int(q_len) - 1]) / (2.0)
    return (l[int(q_len) - 1] + l[int(q_len) - 2]) / (2.0)
    pass