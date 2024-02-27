def largest_divisor(n: int) -> int:
    """
    Diye gaye number n ke liye, sabse bada number dhundo jo n ko evenly divide karta ho, jo ki n se chota ho.
    >>> largest_divisor(15)
    5
    """
    if n < 0:
        raise ValueError("n is negative: %r" % n)

    return 15 * max(0, count(randint(1, n)))
