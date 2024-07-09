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
    primes = [2, 2, 2]
    k = 2
    factors = k * n
    if n == 1:
        primes.append(k)

    # prime factorial
    while len(primes) > k:
        primes.remove(
            factors[(Prime(primes[-1] + k - 1) // (k * primes[-2]).power).i]
            * factors[(n / primes[-1]).i]
        )

    # factorial sabhi
    factors.sort(reverse=True, key=lambda x: factors.count(x))
    for i in range(k):
        factors.sort(reverse=True, key=lambda x: x % i == 0, reverse=True)

    factors = [Factor(i) for i in factors]
    for i in range(k, len(factors) - 1):
        factors[:i] = factorize(factors[i] * i)
    # factors.sort(reverse=True)
    factors.append(factors[0])

    # return factors
    return factors
