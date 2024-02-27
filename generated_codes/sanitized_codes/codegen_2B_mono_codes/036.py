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
    i, r, c = 1, 0, 0
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            c += 1
            r = 10
        elif i % 3 == 0:
            r = 7
        elif i % 5 == 0:
            r = 5
        else:
            r = i
        i += 1
    return r + c