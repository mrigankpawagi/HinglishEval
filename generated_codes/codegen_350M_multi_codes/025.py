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
    prime_factors = [1] * n
    for j in range(n + 1, 0, -1):
        prime_factors[-j] = j
    prime_factors.append(1)
    for j in range(2, n + 1):
        prime_factors[prime_factors[-j] - 1] = j
    return prime_factors[-1]


if __name__ == '__main__':
    print(factorize(26))
    print(factorize(26))
