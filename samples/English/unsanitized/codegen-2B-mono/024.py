

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    d = 1
    while d <= n:
        if n % d == 0:
            return d
            break
        else: d += 1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True,extraglobs={'LargestDivisor':largest_divisor})
