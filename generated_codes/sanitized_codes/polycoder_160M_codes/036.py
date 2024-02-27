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

    def fizz_buzz10(n):
        k = n / 100

        for i in range(n):
            r = r + ((i - 1) * k) if k else (i - 1) * k
            yield (int(r))
        yield s_to(r)
        for i in range(n):
            r = r + (i - n) * k
            yield (int(r))
        yield (r + k + 5)
        yield (int(-r))

    with open("./test/data/buzz10.fizz", "w") as f:
        f.write(str(n))
