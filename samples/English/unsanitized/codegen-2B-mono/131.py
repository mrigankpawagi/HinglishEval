
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 0:
        n = n * -1
    string = str(n)
    i = len(string)
    while(i > 0):
        if i % 2 == 1:
            return sum(int(z) for z in string)
        i -= 1
    return 0


# ------------------------------------------------------------------------
# n! means n x (n-1) x... x 3 x 2 x 1

# Write a function xtimes(n, k) that returns the product of the following:
# 1. The values k each successive times the value n until n reaches 1.
# 2. Starting with n = 1, 1 times k. Each successive call of func(k) returns k times
#    sum of k each successive in the previous call xtimes((n+1), k).
