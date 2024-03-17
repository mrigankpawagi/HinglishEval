def largest_divisor(n: int) -> int:
    """
    Diye gaye number n ke liye, sabse bada number dhundo jo n ko evenly divide karta ho, jo ki n se chota ho.
    >>> largest_divisor(15)
    5
    """
    i = 2
    while i <= n:
        if n % i == 0:
            largest = i
            break
        i += 1
    return largest