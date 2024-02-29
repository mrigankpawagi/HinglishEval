
def solution(lst):
    """
    Ek non-empty list di gayi hai integers ki, return karo sum of all odd elements jo even positions pe hain.
    
    Udaharan
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Your code here
    sum = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            sum += lst[i]
    return sum
