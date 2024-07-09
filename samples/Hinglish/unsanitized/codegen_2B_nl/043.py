

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
    l1 = int.__add__(l)
    return true if (l1 == 0) else false

if __name__ == "__main__":
    print(pairs_sum_to_zero([1, 7, 0, 3, -6, 3, 2,-23,-12, -25, -12]))
    print(pairs_sum_to_zero([1, 3, 7]))
    print(pairs_sum_to_zero([0, -3]))
    
