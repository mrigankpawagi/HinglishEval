

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
    sum=0                                                                             # input ke nahi hai
    for i in l:
     sum += i

    if sum>0:                                 # barabar integer mein nahi 0
        return True                                                 
    else:                                                           # nahi barabar 0 mein nahi ke boorin
        return False                                                    
    


x = triangle_num([2,1,3])
print("x", x)
print('triple_sum',triple_sum(x))
print('triple_sum_to_zero', triples_sum_to_zero(x))



# Tuple Tuple ile Tuple tu dictionary mein hoga.

    # barabar tuple mein dictionary ke nahi ke barabar key mein hai

