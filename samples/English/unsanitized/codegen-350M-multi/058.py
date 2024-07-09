

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    l1[:] = [l1[i] for i in xrange(len(l1)) if l1[i] in l2]
    n = len(l1)
    out = list()
    while n:
        c = 0
        for i in xrange(n + 1):
            if c == len(l2) and l1[i] <= l2[c]:
                out.append(l1[i])
                c += 1
            else:
                break
        else:
            l1[:] = out
            out = []
            n = c
    return l1

if __name__ == '__main__':
    common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    
#E = [19, 18, 9, 5, 1, 1, 5, 5, 6, 1, 6, 3]
#print common(E,[5, 7, 1, 5, 9, 653, 121])
