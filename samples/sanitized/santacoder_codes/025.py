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
    # check type
    assert isinstance(n, int), "Type shouhou be integer"

    # check input integer to not be a prime number
    assert n > 0, "Integer shouhou be atleast 1"

    # check number is prime number
    primes = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103,
        107,
        109,
        113,
        127,
        131,
        137,
        139,
        149,
        151,
        157,
        163,
        167,
        173,
        179,
        181,
        191,
    ]
    prime_flag = True

    for i in range(2, int(n ** (0.5))):
        if n % i == 0 and n >= primes[0] and n <= primes[6]:
            prime_flag = False
            break

    if prime_flag:
        prime_factors = [n]
    else:
        prime_factors = [i for i in range(2, int(n ** (0.5)) + 1) if n % i == 0]

    return prime_factors
