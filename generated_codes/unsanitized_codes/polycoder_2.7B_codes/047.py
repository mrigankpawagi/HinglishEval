

def median(l: list):
    """
    List l ke elements ka median return karo.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    m = max(l)
    n = len(l)
    median = n / 2
    while l[:m - median] == l[median + m:median + median + median - 1:n] and m > 0:
        m -= 1
        median = m
    return l[median + m + (m-median-1)/2]

