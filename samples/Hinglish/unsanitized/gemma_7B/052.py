

def below_threshold(l: list, t: int):
    """
    Agar list l mein saare numbers threshold t se kam hai to True return karo.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for i in l:
        if i >= t:
            return False
    return True


def is_sorted(l: list):
    """
    Agar list l sorted hai to True return karo.
    >>> is_sorted([1, 2, 3, 4])
    True
    >>> is_sorted([1, 2, 4, 3])
    False
    """
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


def is_sorted_2(l: list):
    """
    Agar list l sorted hai to True return karo.
    >>> is_sorted_2([1, 2, 3, 4])
    True
    >>> is_sorted_2([1, 2, 4, 3])
    False
    """
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


def is_sorted_3(l: list):
    """
    Agar list l sorted hai to True return karo.
    >>> is_sorted_3([1, 2, 3, 4])
    True
    >>> is_sorted_3([1, 2, 4, 3])
    False
    """
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


def is_sorted_4(l: list):
    """
    Agar list l sorted hai to True return karo.
    >>> is_sorted_4([1, 2, 3, 4])
    True
    >>> is_sorted_4([1, 2, 4, 3])
    False
    """
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


def is_sorted_5(l: list):
    """
    Agar list l sorted hai to True return karo.
    >>> is_sorted_5([1, 2