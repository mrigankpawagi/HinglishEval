

def below_threshold(l: list, t: int):
    """
    Agar list l mein saare numbers threshold t se kam hai to True return karo.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    if not l:
        return False
    if t <= len(l):
        return False
    return True

# def l_of_list(l: list, x: int):
#     """
#     Lef threshend a number kam na to False.
#     >>> [2, 4, 5, 6].l_of_list(3, 2)
#     [True, False, True, True]
#     >>> [10, 12, 14, 16].l_of_list(5, 2)
#     [True, False, True, True]
#     """
#     return l if x == 0 or (x % 2 == 0 and len(l) > x) else False
