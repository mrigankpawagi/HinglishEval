
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    if n > m: return -1
    return format(int((n+m)/2), '0'+str(0)+'b')

#--------------------------------------------
# H1. A function that returns all the divisors of a number
#
# Question:
#   Given a number number_x, 
#   provide a python function number_divisiors(number_x).
#   Number_x is an integer > 0. 
#     The function should return a list with the divisors
#   of number_x.
#     Example:
#         number_divisiors(25) must return the list: [1, 5, 5, 5, 5, 5, 5, 5]

# solution:
