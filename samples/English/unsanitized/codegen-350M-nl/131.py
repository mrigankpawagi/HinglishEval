
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    for i in range(1, n * 2, 2):
        if i % 2 == 0:
           return i * (i + 1) % 2
    return 0

print(digits(3)) # Prints 15

A:

You need to take out the parentheses, if n is a multiple of 2, and the assignment.
n, is a multiple of 2

