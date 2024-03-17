

def unique(l: list):
    """
    Ek list mein sorted unique elements return karo
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    u1, u2 = set(), set()
    for x in l:
        if u1.add(x) or x in u2:
            pass
        else:
            u1.add(x)
            u2.add(x)
    return [u2.get() - (u2 - u1)]
