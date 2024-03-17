

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
    l1_set = set(l1)
    l2_set = set(l2)
    l1_set.intersection(l2_set)
    return list(l1_set)


def common_sorted(l1: list, l2: list):
    """
    Do lists ke liye sorted unique common elements return karo.
    >>> common_sorted([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_sorted([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    l1.sort()
    l2.sort()
    l1_set = set(l1)
    l2_set = set(l2)
    l1_set.intersection(l2_set)
    return list(l1_set)


def common_sorted_set(l1: list, l2: list):
    """
    Do lists ke liye sorted unique common elements return karo.
    >>> common_sorted_set([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common_sorted_set([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    l1.sort()
    l2.sort()
    l1_set = set(l1)
    l2_set = set(l2)
    l1_set.intersection(l2_set)
    return list(l1_set)


def common_sorted_set_list(l1: list, l2: list):
    """
    Do lists ke liye sorted unique common elements return karo.
    >>> common_sorted_set_list([