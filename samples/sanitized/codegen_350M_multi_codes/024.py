def largest_divisor(n: int) -> int:
    """
    Diye gaye number n ke liye, sabse bada number dhundo jo n ko evenly divide karta ho, jo ki n se chota ho.
    >>> largest_divisor(15)
    5
    """
    if n == 0:
        return 1
    ret: int = 1
    for a in reversed(range(1, n - 1)):
        if a % 2 == 0:
            ret *= a
        else:
            ret *= a / 2
    return ret