
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
 
    n = len(lst)
 
    if n == 1:
        return (int)(lst[0] % 2) * 2
 
    result = 0
 
    for i in range(1, n):
        if (lst[i] % 2) == 0:
            result += 2 * 2 * result + lst[i]
        else:
            result += 2 * result + lst[i]
 
    return (int)(result) / 2
"""
 
 # #
 # #
 #
 # 
 
