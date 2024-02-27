def monotonic(l: list):
    """
    True return karo agar list ke elements monotonically badh rahe ho ya ghat rahe ho.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # initialize index
    l_ind = 0
    l_len = len(l)
    while l_ind < l_len:
        if l[l_ind] >= l[l_ind + 1]:
            return False
        l_ind += 1
    return True