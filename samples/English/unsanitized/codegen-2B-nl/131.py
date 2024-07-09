
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n = abs(n)
    if n % 2:
        return 0
    prod = 1
    for i in range(2, n//2 + 1):
        prod *= (n % 2 == 0 and i % 3 or i % 5 or i % 7)
    return prod % 3

Example:
>>> digits(13567890)
2258769

A:

Python 3.4+ (or C to get the exact same performance):
for i in range(int(math.sqrt(x))+1):
    result += 0 if i in 1..x+1 and (x % (2*i+1) == 0 or i/3 in 1..x+1) else result

