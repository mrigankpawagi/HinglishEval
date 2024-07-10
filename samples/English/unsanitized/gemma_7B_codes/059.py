

def largest_prime_factor(n: int):
    """
    n ka sabse bada prime factor return karo. Maan lo ki n > 1 hai aur yeh prime nahi hai.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # TODO: Implement this function yourself
    prime_factors = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            prime_factors.append(i)
            if not n % (i*i):
                n //= i
            else:
                i += 1
        else:
            i += 1
    return max(prime_factors)
    
def prime_factors(n: int) -> list:
    """
    N ka list of prime factors return karo. Maan lo ki n > 1 aur iski sabhi prime factors different hai.
    >>> prime_factors(13195)
    [5, 7, 13, 29]
    >>> prime_factors(2048)
    [2]
    """
    # TODO: Implement this function yourself
    factors = []
    for i in range(2, n+1):
        k = 2
        while n % i == 0:
            n //= i
            k += 1
        if k != 1:
            factors.append(i)
    return factors
