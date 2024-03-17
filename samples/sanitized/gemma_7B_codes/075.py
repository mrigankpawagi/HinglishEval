
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
        if a % 2 == 0:
            return False
        elif a % 3 == 0:
            return False
        elif a % 5 == 0:
            return False
        else:
            return True
    else:
        return False

