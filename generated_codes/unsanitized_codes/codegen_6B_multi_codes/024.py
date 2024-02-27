

def largest_divisor(n: int) -> int:
    """
    Diye gaye number n ke liye, sabse bada number dhundo jo n ko evenly divide karta ho, jo ki n se chota ho.
    >>> largest_divisor(15)
    5
    """

    count = 0
    d = 2
    while True:
        divisor = abs(n - d) // d
        if divisor % 2 == 0:
            count += 1
        else:
            count += divisor - 1
        if divisor > d and divisor < int(sqrt(n) + 1):
            return d

        d = int(d + 1)
