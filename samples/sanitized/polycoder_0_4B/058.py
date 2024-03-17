def common(l1: list, l2: list):
    """
    Do lists ke liye sorted unique common elements return karo.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    if l1 == l2:
        return l1, l2
    if len(l1) == 1:
        return l2, True

    def sortfunc(a: List, b: List) -> int:
        if a not in l2:
            return l1.index(a)
        return sort_array_by_weight(b, (a, 0), 1, False, False, False)

    s, l, res = sortfunc(l1, l2)
    if res:
        return tuple(map(res, s))
    return l
