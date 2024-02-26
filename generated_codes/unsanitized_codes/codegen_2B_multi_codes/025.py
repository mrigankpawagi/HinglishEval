from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    prime_factors = prime_factors_list(n)
    factorized_numbers = [0] * len(prime_factors)
    for prime_factor in prime_factors:
        for i in range(prime_factor):
            factorized_numbers[prime_factor] += 1
    return factorized_numbers


