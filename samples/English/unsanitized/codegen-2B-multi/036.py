

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return sum([int(_) for _
                in [repr(i)
                    for i in range(max(1, n), (n - 1) / 2 + 1)
                    if any(repr(j) in repr(i)
                           for j in range(11, 13, 11))])])


if __name__ == '__main__':
    import doctest

    doctest.testmod()
