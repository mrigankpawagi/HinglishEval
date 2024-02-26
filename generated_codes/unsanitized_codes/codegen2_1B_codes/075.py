
def is_multiply_prime(a):
    """
    Ek function likho jo true return kare agar diya gaya number 3 prime numbers ka multiplication hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai. 
    Udaharan:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    result = 0
    for i in range(2, a):
        if i**2 == a:
            result += 1
            continue
        if kl(a) == 0 or i % kl(a) == 0:
            return False
    return result < 3


