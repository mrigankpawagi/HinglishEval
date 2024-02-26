

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    for i, d in enumerate(divisors(abs(n))):
        # Note: n is a positive integer, and divisible by d
        if n % d == 0:
            return i + 1
    raise ValueError("n % d == 0 for all {}".format(divisors(abs(n))))

