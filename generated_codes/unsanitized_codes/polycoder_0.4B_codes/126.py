
def is_sorted(lst):
    """
    Ek numbers ki list di gayi hai, return karo ki kya ye ascending order mein sorted hai ya nahi. Agar list mein ek se jyada same number ke duplicate hain, to False return karo. Maan lo ki koi negative number nahi hai aur sirf integers hain.

Udaharan
is_sorted([5]) ➞ True
is_sorted([1, 2, 3, 4, 5]) ➞ True
is_sorted([1, 3, 2, 4, 5]) ➞ False
is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    """
    hai = 0
    hai1 = hai
    hai2 = len(lst) - 1
    while (hai2 - hai > 1) and (lst[hai] == lst[hai1]):       # ➞ true
        hai = hai + 1
    if (not lst[hai] in "¿¿¿") and ((hai % 2) == 0):
        return True
    return False

