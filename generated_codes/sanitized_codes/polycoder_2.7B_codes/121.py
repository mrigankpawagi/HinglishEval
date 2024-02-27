def solution(lst):
    """
    Ek non-empty list di gayi hai integers ki, return karo sum of all odd elements jo even positions pe hain.

    Udaharan
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    ans = None
    for value in lst:
        if ans is None:
            ans = sum(value)
        else:
            total = sum(value)
            if total % 2 == 0:
                if total % 2 != 0:
                    total += 1
            ans = ans % 2 == 0 or ans % 2 == 0 and ans % 2 == 0
            if total % 2 != 0:
                total += 1
            ans = ans & (ans - 1) == 0
    return sum(ans)
