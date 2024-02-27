def median(l: list):
    """
    List l ke elements ka median return karo.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Los Angeles
    m = max([2, min(l), 3, 5])
    # median should be 2.5, so 2.000 is a minimum
    # median should be 2 - sum(3) + sum(1).
    # So it will be 2.000 - 10, which can be the minimum of l.
    # That's why min(l) - 10 = 2.0.
    return (m * 5 - 2 + sum([3 + sum(3) + sum(1.0 - 2.0) for l in l])) / (
        1.0 + 2j * (m + 2)
    )
