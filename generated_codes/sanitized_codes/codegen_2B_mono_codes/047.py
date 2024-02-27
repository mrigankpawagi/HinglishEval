def median(l: list):
    """
    List l ke elements ka median return karo.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # TODO
    if len(l) == 0:
        return None
    half = len(l) // 2
    a = l[:half]
    b = l[half:]
    a.sort()
    b.sort()
    half_a = len(a) // 2
    half_b = len(b) // 2
    if len(a) < len(b):
        ans = a[half_a]
    else:
        ans = b[half_b]
    return ans