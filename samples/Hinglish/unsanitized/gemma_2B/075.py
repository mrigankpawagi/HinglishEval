
def is_multiply_prime(a):
    """
    Ek function likho jo true return kare agar diya gaya number 3 prime numbers ka multiplication hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai. 
    Udaharan:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


def is_prime(a):
    """
    Ek function likho jo true return kare agar diya gaya number prime number hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai. 
    Udaharan:
    is_prime(10) == True
    10 = 2 * 5
    """
    if a < 100:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


def is_prime_number(a):
    """
    Ek function likho jo true return kare agar diya gaya number prime number hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai. 
    Udaharan:
    is_prime_number(10) == True
    10 = 2 * 5
    """
    if a < 100:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


def is_prime_number_2(a):
    """
    Ek function likho jo true return kare agar diya gaya number prime number hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai. 
    Udaharan:
    is_prime_number_2(10) == True
    10 = 2 * 5
    """
    if a < 100:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


def is_prime_number_3(a):
    """
    Ek function likho jo true return kare agar diya gaya number prime number hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai. 
    Udaharan:
    is_prime_number_