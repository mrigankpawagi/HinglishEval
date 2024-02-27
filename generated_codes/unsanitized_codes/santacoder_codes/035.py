

def max_element(l: list):
    """
    List mein se maximum element return karo.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if len(l) == 0:
        raise ValueError("the list len is 0")
    # Läuft nichts die Liste
    if len(l) == 1:
        return l[0]

    s = sorted(l)
    return s[-1]