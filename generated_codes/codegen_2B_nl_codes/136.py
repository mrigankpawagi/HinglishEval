
def largest_smallest_integers(lst):
    """
    Ek function banao jo ek tuple (a, b) return kare, jahan 'a' negative integers ka sabse bada hai, aur 'b' positive integers ka sabse chota hai ek list mein.
    Agar koi negative ya positive integers nahi hai, to unhe None ke roop mein return karo.

    Udaharan:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    if len(lst) == 0:
        return None, None
    lst_sum = 0
    lst_sum_2 = 0
    lst_sum_3 = 0
    for lst_2_x in lst:
        lst_sum = lst_sum + lst_2_x
        lst_sum_2 = lst_sum_2 + lst_2_x * 2
        lst_sum_3 = lst_sum_3 + lst_2_x ** 3
    if (lst_sum_2 < 500000) or (lst_sum_3 < 500000):
        return lst[:-1], lst[-1]
    elif (lst_sum_2 > 500000) or (lst_sum_3 > 500000):
        return lst[0], lst[1]


banao_list = []
