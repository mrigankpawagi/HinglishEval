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
    numbers: List[int] = []
    while n > 1:
        number: int
        while n % 2 == 0:
            n = n // 2
            number = 2
        while n % 5 == 0:
            n = n // 5
            number = 5
        while n % 7 == 0:
            n = n // 7
            number = 7
        numbers = [number] * number
    numbers.sort()
    return numbers


def generate_factors(n: int) -> List[int]:
    """Generate list of factors of integer by checking all non-negative divisors.
    Input number should be equal to product of all factors
    >>> generate_factors(28)
    [1, 2, 4, 7, 14, 28]
    >>> generate_factors(120)
    [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60]
    """
    factors: List[int] = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if n // i != i:
                factors.append(n // i)
    return factors


def prime_factors(n: int, to: int) -> List[int]:
    """Returns list of prime factors of integer between given bounds.
    E.g. prime_factors(-5, 5) => [5]
    >>> prime_factors(9, 20)
    [3, 3]
    """
    factors: List[int] = []
    i = 2
    while n != 1:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i = i + 1
    return factors[1:]


def all_factors(n: int, from_: int, to: int):
    """Return factor list from from_ to .

    >>> from_