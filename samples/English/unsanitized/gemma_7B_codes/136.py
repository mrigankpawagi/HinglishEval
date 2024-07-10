
def largest_smallest_integers(lst):
    """
    Ek function banao jo ek tuple (a, b) return kare, jahan 'a' negative integers ka sabse bada hai, aur 'b' positive integers ka sabse chota hai ek list mein.
    Agar koi negative ya positive integers nahi hai, to unhe None ke roop mein return karo.

    Udaharan:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    neg_int = None
    pos_int = None
    for i in lst:
        if neg_int is None and i < 0:
            neg_int = i
        elif neg_int is not None and i < neg_int:
            neg_int = i
        if pos_int is None and i > 0:
            pos_int = i
        elif pos_int is not None and i > pos_int:
            pos_int = i
    if neg_int is None and pos_int is None:
        return None, None
    else:
        return neg_int, pos_int


print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # (None, 1)
print(largest_smallest_integers([]))  # (None, None)
print(largest_smallest_integers([0]))  # (None, None)


#2
def binary_to_base():
    """
    Ek function banao jo ek integer base aaur ek non-negative integer x ko input le, aur 0 ke upar ka sabse chota integer base aaur 2 ke niche ka sabse bada integer x ke binary btao jaha 1 to power ke roop mein hain.
    Agar any integer is not present, then None ko return karo.

    Udaharan: 

    binary_to_base(4, 2)      ==>  (None, 3)
    binary_to_base(15, 10)    ==>  (2, 13)    
    binary_to_base(2, 4)      ==>  (1, 9)
    """
    for i in range(2, x + 1):
        k, remainder = divmod(x, i)
        if remainder != 0:
            return (i-1, x-k*i)


print(binary_to_base(4, 2))  # (None, 3)
print(binary_to_base(15, 10))  # (2, 13)
print(binary_to_base(2, 4))  # (1, 9)


# 3
def list_sum