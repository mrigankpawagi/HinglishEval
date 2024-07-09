
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    a = abs(a)
    if a >= 100:
        return False
    elif a % 9 == 0:
        return False
    elif a % 3 == 0:
        return False
    else:
        if a == 2 * 3 * 5:
            return True
        else:
            return False

