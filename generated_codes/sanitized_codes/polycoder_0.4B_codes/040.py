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
    karte_list = []
    for lo, hi in itertools.permutations(l):
        # ko output is list of tuple (lo, hi) with each element of the pair in [lo, hi] being true if
        # it's 0 with a true in [lo, hi]
        karte_list.append(tuple(map(lambda x: x[lo], karte_list)))
    return bisect.bisect_left(karte_list, bisect.count(karte_list))
