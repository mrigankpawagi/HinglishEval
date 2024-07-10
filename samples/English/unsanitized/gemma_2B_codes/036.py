

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count = 0
    while n >= 11:
        count += n//11
        n = n % 11
    while n >= 13:
        count += n//13
        n = n % 13
    else:
        count += n //11
    return count
