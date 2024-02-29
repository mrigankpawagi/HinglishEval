

def unique(l: list):
    """
    Ek list mein sorted unique elements return karo
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))


def unique_2(l: list):
    """
    Ek list mein sorted unique elements return karo
    >>> unique_2([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(set(l)))


def unique_3(l: list):
    """
    Ek list mein sorted unique elements return karo
    >>> unique_3([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(dict.fromkeys(l)))


def unique_4(l: list):
    """
    Ek list mein sorted unique elements return karo
    >>> unique_4([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(dict.fromkeys(l)))


def unique_5(l: list):
    """
    Ek list mein sorted unique elements return karo
    >>> unique_5([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(dict.fromkeys(l)))


def unique_6(l: list):
    """
    Ek list mein sorted unique elements return karo
    >>> unique_6([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(dict.fromkeys(l)))


def unique_7(l: list):
    """
    Ek list mein sorted unique elements