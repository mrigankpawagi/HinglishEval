

def largest_prime_factor(n: int):
    """
    n ka sabse bada prime factor return karo. Maan lo ki n > 1 hai aur yeh prime nahi hai.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        return False
    elif n == 2:
        return True
    factor = (2, 3)
    for factor in factor_iter(n, 2):
        if factor > 1:
            break
    else:
        return False

    while n % factor!= 1:
        n /= factor
    return n

factors = prime_finder()
prime_factors = [largest_prime_factor(n) for n in [2, 3, 5, 7, 11, 13, 17, 19, 23]]
print([f for f in factors if f in prime_factors])

OUTPUT:
[(13195, 29), (2048, 2)]

