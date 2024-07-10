
def solution(lst):
    """
    Ek non-empty list di gayi hai integers ki, return karo sum of all odd elements jo even positions pe hain.
    
    Udaharan
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # write your code here
        # if empty list pass error
    if len(lst) == 0:
        return "You cant add sum of empty list numbers"
    sum_ = 0
    for i in range(0, len(lst), 2):
        if lst[i] % 2 == 1:
            sum_ = sum_ + lst[i]
    return sum_
