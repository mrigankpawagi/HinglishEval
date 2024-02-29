

def largest_prime_factor(n: int):
    """
    n ka sabse bada prime factor return karo. Maan lo ki n > 1 hai aur yeh prime nahi hai.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        return 2
    for i in range(2, n):
        if n % i == 0:
            return i
    return n


def is_prime(n: int):
    """
    n ka prime check karo.
    >>> is_prime(13195)
    True
    >>> is_prime(2048)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_factor(n: int, prime: int):
    """
    n ka prime factor check karo.
    >>> is_prime_factor(13195, 29)
    True
    >>> is_prime_factor(2048, 2)
    True
    >>> is_prime_factor(2048, 3)
    False
    """
    if n < 2:
        return False
    if n % prime == 0:
        return True
    return False


def is_prime_factor_list(n: int, prime_list: list):
    """
    n ka prime factor list check karo.
    >>> is_prime_factor_list(13195, [29])
    True
    >>> is_prime_factor_list(2048, [2, 3])
    True
    >>> is_prime_factor_list(2048, [2, 3, 5])
    False
    """
    if n < 2:
        return False
    if n % prime_list[0] == 0:
        return True
    for i in range(1, len(prime_list)):
        if n % prime_list[i] == 0:
            return True
    return False


def is_prime_factor_list_2(n: int, prime_list: list):
    """
    n ka prime factor list check karo.
    >>> is_prime_factor_list_2(13195, [29])
    True
    >>> is_prime_factor