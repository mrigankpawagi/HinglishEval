

def unique(l: list):
    """
    Ek list mein sorted unique elements return karo
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    res = []
    idx_map = {}
    for i in range(1, len(l)):
        if not idx_map.get(l[i]):
            res.append(l[i])
            idx_map[l[i]] = i
        else:
            idx_map[l[i]] += 1
    print(idx_map)
    return res<|python|>import importlib

#