

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
    li = sorted(list(set(l)))
    if li[0]!= 0:
        return 0
    for i in range(1, len(li)):
        if li[i] == li[i-1]:
            li[i] = 0
    if len(li) > 1:
        if li[-1] == 0:
            return False
        if li[-2] == 0:
            return True
    return li[0] == 0
