
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


# Question 2
def is_prime(a):
    """
    Ek function likho jo true return kare agar diya gaya number prime hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai. 
    Udaharan:
    is_prime(30) == False
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


# Question 3
def is_prime_number(a):
    """
    Ek function likho jo true return kare agar diya gaya number prime hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai. 
    Udaharan:
    is_prime_number(30) == False
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


# Question 4
def is_prime_number_2(a):
    """
    Ek function likho jo true return kare agar diya gaya number prime hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai. 
    Udaharan:
    is_prime_number_2(30) == False
    """
    if a < 100:
        if a % 2 == 0:
            return False
        elif a % 3 == 0:
            return False
        elif a % 5 == 0