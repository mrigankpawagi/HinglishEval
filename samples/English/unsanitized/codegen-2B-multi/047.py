

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = l[:]
    l.sort()
    n = len(l)
    if n % 2 == 0:
        if n == 0:
            return 0.0  # empty list
        return (l[(n >> 1) - 1] + l[n >> 1])/2    # even
    else:
        return l[n >> 1]


