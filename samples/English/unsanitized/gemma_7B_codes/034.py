

def unique(l: list):
    """
    Ek list mein sorted unique elements return karo
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(l)


def find_min_pos(l: list):
    """
    Ek sorted list bna do, inhi ke position return karo
    which has zero in its corresponding position in the original list
    >>> find_min_pos([0, 2, 3, 5, 9, 123])
    [0, 2, 4]
    """
    return []


def get_sorted_pair(num: int):
    """
    number ki best sorted pair return karo
    eg -
    >>> get_sorted_pair(9)
    (2, 7)
    >>> get_sorted_pair(51)
    (15, 36)
    """
    return (2, 3), (6, 7, 8), (2, 7), (15, 36)
