def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    count = 0
    for i in range(2, a):
        if a % i == 0 and prime(i):
            count += 1
    if count == 3:
        return True
    else:
        return False