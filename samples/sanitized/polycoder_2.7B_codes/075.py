def is_multiply_prime(a):
    """
    Ek function likho jo true return kare agar diya gaya number 3 prime numbers ka multiplication hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai.
    Udaharan:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a != 3:
        return False

    result = 0
    for i in xrange(a):
        k = i
        for counter in range(3, a):
            k *= counter

        if a % k != 0:
            return False

        result += abs(k % 3)
    return result % 3 == 1
