

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if (n == 1):
        return 1
    else:
        s = prime_factors(n)
        prime_factors = str(n).split("")
        for p in s:
            factor = factor_generator(p, prime_factors)
            if factor > 1:
                s.append(factor)
        return int(len(s))


