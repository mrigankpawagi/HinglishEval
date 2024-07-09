def solution(lst):
    """
    Ek non-empty list di gayi hai integers ki, return karo sum of all odd elements jo even positions pe hain.
    Udaharan
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    res = 0
    count = 0
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
            # print(lst[i], end="")
            count += 1
            res += lst[i]
    if count == 0:
        return 0
    else:
        return res