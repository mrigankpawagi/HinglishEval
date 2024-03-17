

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
    for i in xrange(1, len(l)):
        if l[i]!= 0 and l[i]!= l[-1]:
            return False
    return True


if __name__ == "__main__":
    ans = 0
    data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for i in xrange(1, len(data)):
        a = pairs_diff_sum(data[:i], data[i])
        if a is not None:
            ans += a
    print ans


