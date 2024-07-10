

def below_threshold(l: list, t: int):
    """
    Agar list l mein saare numbers threshold t se kam hai to True return karo.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for i in range(len(l)):
        if t > l[i]:
            return True
    return False

# 
# def below_threshold(l: list, t: int):
#     """
#     Agar list l mein saare numbers threshold t se kam hai to True return karo.
#     >>> below_threshold([1, 2, 4, 10], 100)
#     True
#     >>> below_threshold([1, 20, 4, 10], 5)
#     False
#     """
#     if len(l) == 0:
#         return False
#     elif t > l[0]:
#         return below_threshold(l[1:], t)
#     else:
#         return True

# 
# def below_threshold(l: list, t: int):
#     """
#     Agar list l mein saare numbers threshold t se kam hai to True return karo.
#     >>> below_threshold([1, 2, 4, 10], 100)
#     True
#     >>> below_threshold([1, 20, 4, 10], 5)
#     False
#     """
#     i = 0
#     t = 100
#     while i < len(l):
#         if l[i] < t:
#             i += 1
#         else:
#             return False
#     return True

# 
# def below_threshold(l: list, t: int):
#     """
#     Agar list l mein saare numbers threshold t se kam hai to True return karo.
#     >>> below_threshold([1, 2, 4, 10], 100)
#     True
#     >>> below_threshold([1, 20, 4, 10], 5)
#     False
#     """
#     for i in l:
#         if i < t:
#             t = i
#     return t < 100

# 
# def below_threshold(l: list, t: int):
#     """
#     Agar list l mein saare numbers threshold