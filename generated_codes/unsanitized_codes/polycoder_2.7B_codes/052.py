

def below_threshold(l: list, t: int):
    """
    Agar list l mein saare numbers threshold t se kam hai to True return karo.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    if len(l) == 0:
        return False
    if t%100 == 0:
        print(t)
        print(str(l))
    return str(l) == str(t)

