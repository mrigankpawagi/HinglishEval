

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    for i in range(0, len(l1)):
        for j in range(0, len(l2)):
            common = sum(l1[i]==l2[j]) or -1 # -1 means no common
            if common is not -1:
                return [l1[i]] + common + [l2[j]]
    return []

common([3, 4, 2], [53]*5)
# [3]

A:

