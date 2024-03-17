def common(l1: list, l2: list):
    """
    Do lists ke liye sorted unique common elements return karo.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    l1.sort()
    l2.sort()
    liye = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] == l2[0]:
            liye.append(l1[0])
            del l1[0]
            del l2[0]
        elif l1[0] > l2[0]:
            del l1[0]
        else:
            del l2[0]
    return liye
