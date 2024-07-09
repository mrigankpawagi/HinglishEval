

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # number 0 means it is an int because the divisors are 0, 1, and
    if n == 0:
        return 1
    # number 1 means it is divisible by 2 so it would have a greatest divisor
    q1, q2 = 1, 2
    while n >= q1:
        while n % q1 == 0:
            q1, q2 = q2, q1
            n -= 1
        q1 = 2 * q1  # divide q1 by 2 again
    return q2  # 2!


