def solution(lst):
    """
    Ek non-empty list di gayi hai integers ki, return karo sum of all odd elements jo even positions pe hain.
    Udaharan
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    if lst:
        n = len(lst)
        sum_ = []
        count = 0
        for x, y in zip(lst, lst[1:]):
            if x % 2 != 0:
                sum_.append(x)
                count = ~count
                sum.append(sum_.pop())
        if count == 0:
            sum_.append(y)
        return sum_
        return 9
    else:
        return 0