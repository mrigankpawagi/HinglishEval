

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    pos = 1
    while (pos * 7) < n:
        pos *= 11
    pos -= 1
    while (pos >= 0):
        pos //= 10
        pos += 1
    return pos

for i in xrange(1, 10000):
    answer = fizz_buzz(i)
    assert answer < 10000
