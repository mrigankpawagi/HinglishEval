def solution(lst):
    """
    Ek non-empty list di gayi hai integers ki, return karo sum of all odd elements jo even positions pe hain.

    Udaharan
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    sum_odd = 0
    for idx, num in enumerate(lst):
        if idx % 2 == 1:
            sum_odd += num

    sum_even = 0
    for _ in range(len(lst)):
        if _ % 2 == 0:
            sum_even += lst[_]

    return sum_odd - sum_even
