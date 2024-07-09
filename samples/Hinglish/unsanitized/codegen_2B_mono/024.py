

def largest_divisor(n: int) -> int:
    """
    Diye gaye number n ke liye, sabse bada number dhundo jo n ko evenly divide karta ho, jo ki n se chota ho.
    >>> largest_divisor(15)
    5
    """
    while n!= 1:
        n = factor(n)
        if n!= 1:
            n %= 1
    return n
