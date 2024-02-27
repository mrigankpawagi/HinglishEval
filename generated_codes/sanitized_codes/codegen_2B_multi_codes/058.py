

def common(l1: list, l2: list):
    """
    Do lists ke liye sorted unique common elements return karo.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """   for elem in l1:
        if elem not in l2:
            return [elem]
    for elem in l2:
        if elem not in l1:
            return [elem]
    return list({l1[0]: None, l2[0]: None}.keys())
