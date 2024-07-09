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
    return (
        "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else "Fizz" if n % 11 == 0 else n
    )