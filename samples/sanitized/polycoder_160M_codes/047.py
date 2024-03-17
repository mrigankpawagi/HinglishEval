def median(l: list):
    """
    List l ke elements ka median return karo.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    i = ordered.index(len(l))
    if i >= len(l) - 1:
        # return sorted dict of (kara number, kara number)
        return sorted(l[i], key=operator.itemgetter(0))
    return l[i]
