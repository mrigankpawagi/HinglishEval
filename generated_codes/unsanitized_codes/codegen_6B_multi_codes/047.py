

def median(l: list):
    """
    List l ke elements ka median return karo.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    if len(l) % 2!= 0:
        return l[(len(l) // 2) + int(bool(len(l) % 2))]
    return float(l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0


