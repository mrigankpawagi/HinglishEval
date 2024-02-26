
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 *... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    ret = []  # ret is to hold the return after for loop
    for i in range(1, n+1):
        for j in range(0, i):
            ret.append(j)
            ret.append(i)
        ret.append(1)
    return ret



# f(5) == [1, 2, 6, 24, 15]

# fact(1) == 1
# fact(2) == 2
# fact(3) == 6   
# fact(4) == 24
# fact(5) == 120
# fact(6) == 360
# fact(7) == 1440
# fact(8) == 4320
# fact(9) == 1680
