

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero ek integers ki list ko input ke roop mein leta hai.
    Yeh True return karta hai agar list mein do alag elements hote hain jo
    zero ke barabar sum karte hain, aur anyatha False.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """

    l.sort()
    i = 0
    j = len(l) - 1

    while i < j:
        if l[i] + l[j] == 0:
            return True
        elif l[i] + l[j] > 0:
            j -= 1
        else:
            i += 1
    return False
