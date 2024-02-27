
def solution(lst):
    """
    Ek non-empty list di gayi hai integers ki, return karo sum of all odd elements jo even positions pe hain.
    
    Udaharan
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    odd = 0
    sum = 0
    for i in lst:
        if i % 2 == 1:
            odd += i
            #if i == 3:
            #    print "summ", sum
        sum += i
    return odd
