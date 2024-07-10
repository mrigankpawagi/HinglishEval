

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

    for i in range(len(l)):
        for j in range(i, len(l)-1):
            for k in range(j+1, len(l)):
                if sum(l[i], l[j], l[k]) == 0:
                    return True
    return False

from functools import reduce
def triples_sum_to_zero_v2(l: list):
    """
    triples_sum_to_zero ek integers ki list ko input ke roop mein leta hai.
    Yeh True return karta hai agar list mein teen distinct elements hain jo
    zero ke barabar sum karte hain, aur anyatha False.

    >>> triples_sum_to_zero_v2([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero_v2([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero_v2([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero_v2([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero_v2([1])
    False
    """
    
    for i in l:
        a = list(filter(lambda y: i+y+1 in l, l))
        b = list(filter(lambda x: x + i+1 in l, l))
        c = list(filter(lambda z: i + z+1 in l, l)) 
        d = (reduce(lambda x,y: x+y, a))
        e = (reduce(lambda x,y: x+y, b))
        f = (reduce(lambda x,y: x+y, c))
        if d < 0:
            return True
        elif e < 0:
            return True
        elif f < 0:
            return True
    return False



print(triples_sum_to_zero([1, 3, 5, 0]))
print(triples_sum_to_zero([1, 3, -2, 1]))
print(triples_sum_to_zero