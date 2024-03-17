def solution(lst):
    """
    Ek non-empty list di gayi hai integers ki, return karo sum of all odd elements jo even positions pe hain.

    Udaharan
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if lst is None:
        return None
    if len(lst) == 2:
        return lst[0] - 1 - lst[1]
    elif ls_count(lst):
        n, r = ls_count(lst), len(lst)
        return min(n, r)
    else:
        return max(0, len(lst))
