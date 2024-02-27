def below_threshold(l: list, t: int):
    """
    Agar list l mein saare numbers threshold t se kam hai to True return karo.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    count = 0
    if l[-1] == t:
        return True
    elif len(l) >= 10:
        for i in range(len(l) - 1):
            if l[i] < (l[i + 1]):
                count += 1
                if count >= 4:
                    return True
    else:
        return False