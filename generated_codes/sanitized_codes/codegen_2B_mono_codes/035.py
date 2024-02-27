def max_element(l: list):
    """
    List mein se maximum element return karo.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    max = l[0]
    i = 1
    while i < len(l):
        if l[i] >= max:
            max = l[i]
        i += 1
    return max