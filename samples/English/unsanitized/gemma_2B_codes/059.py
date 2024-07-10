

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Your code here
    if n in (2, 3, 5, 7):
        return n
    result = 2
    x = result
    while x*(x)<=n:
        checkIt = n%x
        if(not(checkIt==0)): result+=1; break
        else: x+=1
        checkIt = x
    if result in (1+x): return result
    else: return x
