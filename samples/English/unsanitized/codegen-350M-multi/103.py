
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
    # Your code here
    if n == 0 or m == 0 or n == m == m == 1:
        return 0
    n2 = m-n
    while n2 > 0:
        n2 = n2 // 2
    rval = 0
    for i in range(n - n / 2):
        rval += i * i
    n2 = n - rval
    for i in range(m - m / 2):
        rval += i * i
    rval %= m
    return rval


