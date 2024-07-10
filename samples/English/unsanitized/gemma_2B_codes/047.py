

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    """Implement this method.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    >>> median([(-1, 99), (2, 5)])
    2.5
    >>> median([(-1, 99), (24, 500), (5, 3), (10, 1), (24.3, 50.0)])
    24.3
    >>> median([(24, 500), (2, 5)])
    2.5
    """
    return (len(l)%2) and l[int(len(l)/2)].key or float(l[len(l)/2-1].key) + float(l[len(l)/2].key) / 2

#median([3, 1, 2, 4, 5]) == 3


#median([-10, 4, 6, 1000, 10, 20])

max(l)
