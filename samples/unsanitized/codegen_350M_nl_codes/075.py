
def is_multiply_prime(a):
    """
    Ek function likho jo true return kare agar diya gaya number 3 prime numbers ka multiplication hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai. 
    Udaharan:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if (str(a)!= 'number'):
        return False
    else:
        return (is_prime(a) and not is_prime(a) and a.isdigit())


