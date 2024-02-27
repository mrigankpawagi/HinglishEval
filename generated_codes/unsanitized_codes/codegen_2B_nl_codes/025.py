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
    a = 2
    b = 3
    c = 1
    res = [a]
    while c * c - b * b <= n:
        res.append(b)
        b = b // (-b ** 2 + c * c - 2 * c) ^ 1 / c
    return res
