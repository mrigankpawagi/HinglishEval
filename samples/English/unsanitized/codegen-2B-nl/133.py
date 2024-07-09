

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    a = 0
    b = 0
    for ii in range(len(lst)):
        a += lst[ii] * lst[ii]
        b += lst[ii] * lst[ii]
    return a*a/2 + b*b/2

from sympy import *

for i in range(100):
    print a_sum_squares(lst1[i],lst2[i])
    a_sum_squares.n(lst1[i],lst2[i])
