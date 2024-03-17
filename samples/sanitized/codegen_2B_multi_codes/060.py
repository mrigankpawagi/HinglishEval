

def sum_to_n(n: int):
    """
    sum_to_n ek function hai jo 1 se lekar n tak ke numbers ka sum karta hai.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """   if n == 0:
        return 1

    # base sum is start with the num1
    base = sum_to_n(n / 2, n % 2)
    while (n / 2) > 0:
        # number of digits in base
        num = n // 2
        # remove all trailing digits
        base -= pow(num, n - num + 1)
        # rearrange value for next call
        n = n - (2 * num)
    return base

