

def common(l1: list, l2: list):
    """
    Do lists ke liye sorted unique common elements return karo.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    result = {}
    #print result

    for i, elem in enumerate(l1):
        for k, val in elem.items():
            try:
                if val == elem[0]:
                    result[k] = sum(x for x in elem[1:])
            except ValueError:
                pass
        else:
            continue
        #result = result[k]
    return result