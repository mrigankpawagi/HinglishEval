

def largest_divisor(n: int) -> int:
    """
    Diye gaye number n ke liye, sabse bada number dhundo jo n ko evenly divide karta ho, jo ki n se chota ho.
    >>> largest_divisor(15)
    5
    """
    if n <= 1:
        return 0
    elif n < 3:
        raise ValueError("bad division numbers, n must be between 1 and 3 inclusive")
    elif n < 3 ** 2:
        raise ValueError("bad division numbers, n must be between 1 and 3 inclusive")
    return (n if n == 1 else n - 1) // 2

