

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n <= 1:
        raise TypeError("You can only check prime numbers")
    while (n % 2 == 0) == True:
        n = int(n / 2)
    for a in range(3, int(n ** 0.5) + 1, 2): 
        if n % a == 0:
            return False
    return True
        
p = 0
s = 0
for p in range(101):
    if is_prime(p) == True:
        for s in range(p):
            if is_prime(s):
                print(s)
                break
        print(s)
        print(p)
        break
