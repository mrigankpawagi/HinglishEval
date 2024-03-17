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
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
