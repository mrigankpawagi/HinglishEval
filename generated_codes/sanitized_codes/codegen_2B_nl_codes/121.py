def solution(lst):
    """
    Ek non-empty list di gayi hai integers ki, return karo sum of all odd elements jo even positions pe hain.
    Udaharan
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if not lst:
        return 0  # If no list, return 0.
    m = len(lst)  # Minimum length
    if m < 2:
        return 0
    n = len(lst) - 1  # Maximum length
    if m >= n:
        return 0
    sum = 0
    for k in range(m):
        if k % 2 == 1:
            sum += lst[k]
    return sum