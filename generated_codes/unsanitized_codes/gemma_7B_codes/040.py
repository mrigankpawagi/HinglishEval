def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero ek integers ki list ko input ke roop mein leta hai.
    Yeh True return karta hai agar list mein teen distinct elements hain jo
    zero ke barabar sum karte hain, aur anyatha False.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    l.sort()
    for i in range(len(l) - 2):
        if l[i] > 0:
            return False
        if l[i] == l[i + 1] == l[i + 2]:
            return False
        if l[i] + l[i + 1] + l[i + 2] == 0:
            return True
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
