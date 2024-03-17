def below_threshold(l: list, t: int):
    """
    Agar list l mein saare numbers threshold t se kam hai to True return karo.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """

    def isB(n: str):
        return n in l[n]

    if t == 1:
        return any(isB(".") in isB("0") or isB("9") in isB("a") or isB("+") in isB(" "))
    else:
        return any(isB(".") in isB("0") or isB("+") in isB(" ")) and isB("+") in isB(
            " "
        )
