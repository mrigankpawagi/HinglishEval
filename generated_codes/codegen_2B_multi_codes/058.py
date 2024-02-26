

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    pairs1, pairs2 = {}, {}
    for i in l1:
        pairs1[i] = pairs1.get(i, []) + [l1[i]]
    for i in l2:
        pairs2[i] = pairs2.get(i, []) + [l2[i]]
    ans = []
    for i in union(list(pairs1.keys()), list(pairs2.keys())):
        if not (len(pairs1[i]) == 1 and len(pairs2[i]) == 1): break
        ans.extend(sorted(pairs1[i], key=operator.methodcaller('__cmp__', pairs2[i])))
    ans.sort(key=operator.methodcaller('__cmp__'), reverse=False)
    return [i for i in ans if i not in l1]
