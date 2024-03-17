

def below_threshold(l: list, t: int):
    """
    Agar list l mein saare numbers threshold t se kam hai to True return karo.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # First take the index of each member of l that are greater than or
    # equal to t.
    result = None
    index = {}
    for i in l:
        if i >= t:
            index[i] = i  # Map the index to each number such that t < index(s)[i]
        else:
            index[i] = None  # Not an index: do nothing
    # And iterate over the un-indexed members.
    result = True if None in index else False
    # Otherwise (i > t): remove indexing so the result is that of iterating
    # over l unchanged.
    return result


