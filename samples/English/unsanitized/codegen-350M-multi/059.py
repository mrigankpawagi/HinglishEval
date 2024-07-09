

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    factors = []
    while n > 1:
        if n % 2 == 1:
            factors.append(2)
        elif n % 3 == 1:
            factors.append(4)
        else:
            factors.append(n // 10)
        n = n_multipier(factors, n)

    return n


