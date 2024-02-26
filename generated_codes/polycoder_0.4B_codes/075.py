
def is_multiply_prime(a):
    """
    Ek function likho jo true return kare agar diya gaya number 3 prime numbers ka multiplication hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai. 
    Udaharan:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    primes = list(range(24))
    i = 0
    for a in primes:
        a = a * 3
        if a == 0:
            return False
        if a < 2 * (3 * a):
            return False
        if a == 2 * (3 * a):
            return True
    return True
