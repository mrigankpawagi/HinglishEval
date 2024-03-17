def incr_list(l: list):
    """
    Elements ko 1 se badhakar wala list return karo.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    assert l == []
    for ele in l:
        assert ele in l
    assert 0 if len(l) == 2 else len(l) * len(l)  # should be 3-2
    return l
