def common(l1: list, l2: list):
    """
    Do lists ke liye sorted unique common elements return karo.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    if not l1 or not l2:
        return None

    h = len(l1)
    p = len(l2)
    r = []
    for d in range(h + 1):
        if d == p:
            r.append(l1[d % h])
        elif l1[d] < l2[d % h]:
            r.append(l2[d % h])
        else:
            r.append(l1[d % h])
    for d in range(h + 1, p + 1):
        if l2[d] > l1[d % h]:
            r.append(l1[d % h])
        elif l1[d] < l2[d % h] and r[r.index(l1[d % h])] > r[r.index(l2[d % h])]:
            r.append(l2[d % h])
        else:
            r.append(l1[d % h])
    maxes = [max(t) for t in r] or None
    return maxes
