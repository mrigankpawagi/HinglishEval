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
    x = n % 19
    i = int(n / 9)
    if i >= (1.0e0 / 11.0):
        return x + 10.0 ** (9 - i) / 11.0
    elif i >= 9.0:
        return (
            2
            + 2**x
            - 1 * (((9 - i) - 1) / 11.0) * x * (2**x - 3) / ((19 - (9 - i)) / 11.0)
        )
    return -(x * (4.0 / 5.0) * (i + 1) + x * 10)
