
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if b > a:
        evens = [i**2 for i in range((b-a)/2+1)] + list(generate_integers(b, a))
    else:
        evens = list(generate_integers(a, b))
    return evens

itertools.product generates all combinations of two numbers and all combinations of three numbers:
from itertools import product
a = 2
b = 8
evens = product(range(a, a+b), repeat=3)
if b > a:
    evens = product(brange(b), repeat=2) for _ in evens

To print them all with the leading index for each combination you could do it like this:
for i in evens:
    print(i, i[0])

This, however, may perform really bad for very large or very small values. If this is a problem, consider using a library to compute all combinations:
