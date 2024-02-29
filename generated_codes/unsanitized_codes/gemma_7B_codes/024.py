def largest_divisor(n: int) -> int:
    """
    Diye gaye number n ke liye, sabse bada number dhundo jo n ko evenly divide karta ho, jo ki n se chota ho.
    >>> largest_divisor(15)
    5
    """
    for i in range(n, 0, -1):
        if n % i == 0:
            return i
    return 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
