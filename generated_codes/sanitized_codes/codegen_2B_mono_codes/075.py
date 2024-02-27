def is_multiply_prime(a):
    """
    Ek function likho jo true return kare agar diya gaya number 3 prime numbers ka multiplication hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai.
    Udaharan:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    a = int(a)
    b = a
    c = a * 10
    while a < 10:
        b = a * 10
        c = (b % 1) + c
        a = int(b // 1)
    if c == b:
        return True
    else:
        return False