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
    total = 2
    while n != 1:
        if n == 1:
            factors.append(1)
        elif n < 4:
            if n == 2:
                factors.append(2)
            else:
                factors.append(3 * n)
        else:
            remainder = n % 2
            for i in range(3, int(n**0.5) + 1, 4):
                remainder = (n - i**2) % i
                if remainder == 0:
                    factors.append(i)
                    break
            else:
                if n < 0:
                    factors.append(-1)
                else:
                    factors.append(2 * n)
        n = n // 2
    return factors
