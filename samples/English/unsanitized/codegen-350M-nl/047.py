

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    result = sum([1 for _, i in itertools.product(_, l)])  # => -0.5
    return result[0]                                           # => 10

I think it's quite easy as a template matching but that's just a matter of taste at this point.
(for example:
