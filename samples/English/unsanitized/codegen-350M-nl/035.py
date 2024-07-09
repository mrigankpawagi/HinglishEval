

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if len(l) == 0:
        return len(lminus1)
    if len(lminus1) == 0:
        return max_element(paddedlplus1 + l)
    #if len(lminus1) > len(l) - 1:
        #    return max_element([1])
    n_leaves = len(lminus1 - l)
    if 0 <= n_leaves <= len(lminus1):
        return max_element(paddedlminus1)
    else:
        #if n_leaves == 0 and len(lminus1) == 0:
        #     return max_element(lminus1)
        #print lminus1
        #return max_element(lminus1 + l)
        #return max(lplus1)
        #return max_element([] + [lminus1])
        #print lminus1
    return max_element(plast + l)

