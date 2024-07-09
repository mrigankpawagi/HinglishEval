

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    result = 0
    for i in range(2, n):
        if is_divisible_by_7(i) and is_divisible_by_11(i) or\
           is_divisible_by_13(i):
            result += 1
    return result


