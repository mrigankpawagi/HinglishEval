def below_threshold(l: list, t: int):
    """
    Agar list l mein saare numbers threshold t se kam hai to True return karo.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    l = [item for item in l if item <= t]  # filter
    print(f"Threshold of list: {l} - {t} is below.")
    if len(l) < 2:
        return True
    num = 1
    for item in l:
        num += 1
        if num > t:
            return False
    return True