

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
    if len(l) == 0:
        return True
    if len(l) == 1:
        return True
    if l[0] > l[1]:
        return False
    if l[0] < l[1]:
        return monotonic(l[1:])
    return monotonic(l[1:])


def is_sorted(l: list):
    """
    True return karo agar list sorted hai.
    >>> is_sorted([1, 2, 3, 4])
    True
    >>> is_sorted([1, 2, 4, 3])
    False
    >>> is_sorted([1, 2, 3, 4, 5])
    True
    """
    if len(l) == 0:
        return True
    if len(l) == 1:
        return True
    if l[0] > l[1]:
        return False
    return is_sorted(l[1:])


def is_sorted_2(l: list):
    """
    True return karo agar list sorted hai.
    >>> is_sorted_2([1, 2, 3, 4])
    True
    >>> is_sorted_2([1, 2, 4, 3])
    False
    >>> is_sorted_2([1, 2, 3, 4, 5])
    True
    """
    if len(l) == 0:
        return True
    if len(l) == 1:
        return True
    if l[0] < l[1]:
        return False
    return is_sorted_2(l[1:])


def is_sorted_3(l: list):
    """
    True return karo agar list sorted hai.
    >>> is_sorted_3([1, 2, 3, 4])
    True
    >>> is_sorted_3([1, 2, 4, 3])
    False
    >>> is_sorted_3([1, 2, 3, 4, 5])
    True
    """
    if len(l) == 0:
        return True
    if len(l) == 1:
        