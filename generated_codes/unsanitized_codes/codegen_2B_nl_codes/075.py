
def is_multiply_prime(a):
    """
    Ek function likho jo true return kare agar diya gaya number 3 prime numbers ka multiplication hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai. 
    Udaharan:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    isPrime = False
    is_a_prime = False
    limit = int(math.sqrt(a))
    for m in range(2, limit + 1):
        if a % m == 0 and isPrime is False:
            isPrime = True
            is_a_prime = False

        if is_a_prime is False:
            break

    return isPrime



