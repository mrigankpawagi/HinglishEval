

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    seen = []
    return [x for x in sorted(set(l), key=l.index) if not (x in seen or seen.append(x))]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
