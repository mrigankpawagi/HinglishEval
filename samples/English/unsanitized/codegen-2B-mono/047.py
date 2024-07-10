

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    if not l:
        raise ValueError("The list is empty")
    middle = len(l) // 2
    median = l[middle]
    return median

