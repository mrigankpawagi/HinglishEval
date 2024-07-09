

def common(l1: list, l2: list):
    """
    Do lists ke liye sorted unique common elements return karo.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    l = []
    for i in l1:
        if not l in l2 or i not in l2:
            l.append(i)
    return l

print(common([1, 8, 10, 54, 7, 1, 14, 9, 3, 9, 5, 9, 5], [2, 6, 1, 3, 4, 6, 2, 3, 9, 10, 9, 4]))

