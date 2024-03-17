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
    sum_of_all_elements = 0
    for value in l:
        if value > 0:
            sum_of_all_elements += value
    if sum_of_all_elements > 0:
        return False
    else:
        return True


# print(triples_sum_to_zero([1, -3, -2, 5]))
print(triples_sum_to_zero([1, 2, 3, 7]))
