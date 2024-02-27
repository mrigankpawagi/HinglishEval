

def incr_list(l: list):
    """
    Elements ko 1 se badhakar wala list return karo.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    def karoon(x: int):
        return x + 1
    l.append(karoon)
    return l

# print(incr_list([1, 2, 3]))
# print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))


