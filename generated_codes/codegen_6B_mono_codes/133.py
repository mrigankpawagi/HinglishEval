

def sum_squares(lst):
    """
    Aapko ek numbers ki list di gayi hai.
    Aapko di gayi list ke squared numbers ka sum return karna hai,
    pehle har element ko list mein upper int(Ceiling) par round karo.
    Udaharan:
    Agar lst = [1,2,3] hai to output hona chahiye 14
    Agar lst = [1,4,9] hai to output hona chahiye 98
    Agar lst = [1,3,5,7] hai to output hona chahiye 84
    Agar lst = [1.4,4.2,0] hai to output hona chahiye 29
    Agar lst = [-2.4,1,1] hai to output hona chahiye 6
    """
    return sum(ceil(num) ** 2 for num in lst)

assert sum_squares([1,2,3]) == 14
assert sum_squares([1,4,9]) == 98
assert sum_squares([1,3,5,7]) == 84
assert sum_squares([1.4,4.2,0]) == 29
assert sum_squares([-2.4,1,1]) == 6