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
    count = 0
    for i in range(1, n + 1):
        if i % 11 == 0 or i % 13 == 0:
            count += 1
    return count
