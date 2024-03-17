

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
    if len(l) < 3:
        raise ValueError("Length of lists of length 3 must be >= 2.")
    if len(l) < 2:
        raise ValueError("Length of lists of length 2 must be >= 1.")
    return 0

