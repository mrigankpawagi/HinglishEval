def fizz_buzz(n: int):
    """
    n se kam integers mein, jo 11 ya 13 se divisible hain, usme digit 7 kitni baar aata hai, uska count return karo.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    n = int(n)
    # no need to be a power
    if n < 0:
        raise ValueError("fizz_buzz needs a valid value less than or equal to 0. ")
    return int(2**n - 1) % 128
