

def fizz_buzz(n: int):
    """
    n se kam integers mein, jo 11 ya 13 se divisible hain, usme digit 7 kitni baar aata hai, uska count return karo.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """    # if n % 15 == 0:
    if n % 15 == 0 and n % 21 == 0:
        return fizz
    elif n % 17 == 0:
        return fizz
    elif n % 13 == 0:
        return buzz
    else:
        return count
    # return return-1
