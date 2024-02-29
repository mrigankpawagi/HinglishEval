

def below_threshold(l: list, t: int):
    """
    Agar list l mein saare numbers threshold t se kam hai to True return karo.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(x < t for x in l)


def above_threshold(l: list, t: int):
    """
    Agar list l mein saare numbers threshold t se bada hai to True return karo.
    >>> above_threshold([1, 2, 4, 10], 100)
    False
    >>> above_threshold([1, 20, 4, 10], 5)
    True
    """
    return all(x > t for x in l)


def in_range(l: list, t1: int, t2: int):
    """
    Agar list l mein saare numbers t1 se t2 se bada hai to True return karo.
    >>> in_range([1, 2, 4, 10], 100, 1000)
    True
    >>> in_range([1, 20, 4, 10], 5, 10)
    True
    >>> in_range([1, 20, 4, 10], 5, 100)
    False
    """
    return all(x in range(t1, t2) for x in l)


def in_range_2(l: list, t1: int, t2: int):
    """
    Agar list l mein saare numbers t1 se t2 se bada hai to True return karo.
    >>> in_range_2([1, 2, 4, 10], 100, 1000)
    True
    >>> in_range_2([1, 20, 4, 10], 5, 10)
    True
    >>> in_range_2([1, 20, 4, 10], 5, 100)
    False
    """
    return all(x in range(t1, t2) for x in l)


def in_range_3(l: list, t1: int, t2: int):
    """
    Agar list l mein saare numbers t1 se t2 se bada hai to True return karo.
    >>> in_range_3([1, 2, 