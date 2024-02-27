

def largest_prime_factor(n: int):
    """
    n ka sabse bada prime factor return karo. Maan lo ki n > 1 hai aur yeh prime nahi hai.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n == 1:
        return 1
    if n <= 3:
        return n
    dp = [3]
    for i in range(n):
        f = int(random.random() * (n // i - 1) * i)
        dp.append(f)
    return max(dp)

