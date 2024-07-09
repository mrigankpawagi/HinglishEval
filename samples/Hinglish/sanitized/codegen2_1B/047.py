

def median(l: list):
    """
    List l ke elements ka median return karo.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    low = len(l) // 2
    mid = len(l) // 2 - (2 * low)
    return l[mid - low][0]

