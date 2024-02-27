

def unique(l: list):
    """
    Ek list mein sorted unique elements return karo
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """   seen_set = set()
    seen_list = []
    for e in l:
        if e not in seen_set:
            seen_set.add(e)
            seen_list.append(e)
    return seen_list
