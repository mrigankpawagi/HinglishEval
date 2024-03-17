def below_threshold(l: list, t: int):
    """
    Agar list l mein saare numbers threshold t se kam hai to True return karo.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return sum(1 for x in l if x <= t) >= len(l)