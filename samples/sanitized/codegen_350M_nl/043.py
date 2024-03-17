

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
    if (len(l) == 0):
        return True
    else:
        for i in range(len(l)):
            k = (i % 2) == 0? 1 : -1
            k = k + 1
            for j in range(i / 2):
                k = k - 1

            if k == 0:
                return True
            # print(l[i])
        return False


