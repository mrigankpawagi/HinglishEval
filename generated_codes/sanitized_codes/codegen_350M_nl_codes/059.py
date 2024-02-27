

def largest_prime_factor(n: int):
    """
    n ka sabse bada prime factor return karo. Maan lo ki n > 1 hai aur yeh prime nahi hai.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    a := n % 2
    k : int
    if k < a + k:
        k = k % 2
    # if k is not a power of 2
    if k <= a :
        return k
    # else
    elif k < a + k * (n % 2):
    # else
    return k + 1
