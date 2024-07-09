def is_multiply_prime(a):
    """
    Ek function likho jo true return kare agar diya gaya number 3 prime numbers ka multiplication hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai.
    Udaharan:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    res = True
    for i in range(1, a / 2 + 1):
        for k in range(2, a / i + 1):
            if a % (k * i) != 0:
                res == False
                break
    return res