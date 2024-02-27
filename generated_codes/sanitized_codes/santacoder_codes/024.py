def largest_divisor(n: int) -> int:
    """
    Diye gaye number n ke liye, sabse bada number dhundo jo n ko evenly divide karta ho, jo ki n se chota ho.
    >>> largest_divisor(15)
    5
    """
    divisor_list = [k for k in range(1, int(n**0.5) + 1) if n % k == 0]
    return (
        divisor_list[0] if len(divisor_list) == 1 else largest_divisor(divisor_list[1])
    )
