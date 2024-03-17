from typing import List


def factorize(n: int) -> List[int]:
    """
    Diye gaye integer ke prime factors ki list return karo, order chhote se bade tak hona chahiye.
    Har ek factor ko utni baar list mein hona chahiye jitni baar wo factorization mein aata hai.
    Input number sabhi factors ka product hona chahiye
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n > 1:
        factor = n
        while factor % 2 == 0:
            factors.append(2)
            factor /= 2
        while factor % 5 == 0:
            factors.append(5)
            factor /= 5
        n = factor
    return factors


def is_prime(n: int) -> bool:
    """
    Input number ke prime factors ki list return karo.
    Input number sabhi factors ka product hona chahiye
    >>> is_prime(8)
    True
    >>> is_prime(25)
    True
    >>> is_prime(70)
    True
    >>> is_prime(100)
    False
    """
    factors = factorize(n)
    return all(factors)


def is_prime_naive(n: int) -> bool:
    """
    Input number ke prime factors ki list return karo.
    Input number sabhi factors ka product hona chahiye
    >>> is_prime_naive(8)
    True
    >>> is_prime_naive(25)
    True
    >>> is_prime_naive(70)
    True
    >>> is_prime_naive(100)
    False
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_fast(n: int) -> bool:
    """
    Input number ke prime factors ki list return karo.
    Input number sabhi factors ka product hona chahiye
    >>> is_prime_fast(8)
    True
    >>> is_prime_fast(25)
    True
    >>> is_prime_fast(70)
    True
    >>> is_prime_fast(100)
    False
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_fast_2(n: int) -> bool:
    """
    Input number ke prime