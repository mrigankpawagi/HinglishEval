

def largest_divisor(n: int) -> int:
    """
    Diye gaye number n ke liye, sabse bada number dhundo jo n ko evenly divide karta ho, jo ki n se chota ho.
    >>> largest_divisor(15)
    5
    """
    if n <= 0:
        return 1

    if n == 1:
        return 1

    i = 2
    n_dividers = 0
    while n_dividers != n:
        if n % i == 0:
            n_dividers = n/i
            print(n/i)
    return i
