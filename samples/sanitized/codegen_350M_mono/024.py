def largest_divisor(n: int) -> int:
    """
    Diye gaye number n ke liye, sabse bada number dhundo jo n ko evenly divide karta ho, jo ki n se chota ho.
    >>> largest_divisor(15)
    5
    """
    divisor = []
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
    if len(divisor) != 0:
        divisor[-1] = n // divisor[0]
        divisor.remove(n // divisor[0])
        return max(divisor)
    else:
        return 0