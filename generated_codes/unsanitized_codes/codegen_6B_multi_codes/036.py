

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
    for a in range(1, n // 3 + 1):
        for b in range(1, n // 3 + 1):
            c = a * b
            if n % (c) == 0:
                count += 1
                # print("{0} == {1}".format(c,n))
    return count


