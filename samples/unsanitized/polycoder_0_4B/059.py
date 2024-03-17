

def largest_prime_factor(n: int):
    """
    n ka sabse bada prime factor return karo. Maan lo ki n > 1 hai aur yeh prime nahi hai.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    k = 2047 * abs(n)
    p = 2 ** 31
    result = k
    if n < 2:
        # prime smaller than prime factor
        while k > 1:
            result = result * p
            k -= p
    try:
        # prime bigger than prime factor
        while k < 0:
            result = result * p
            k += p
        result = result * p
        return result
    except ValueError:
        pass
    # largest prime factor
    return k * p

