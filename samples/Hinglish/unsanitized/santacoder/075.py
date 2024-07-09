
def is_multiply_prime(a):
    """
    Ek function likho jo true return kare agar diya gaya number 3 prime numbers ka multiplication hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai. 
    Udaharan:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    """Kare is_sum_prime_numbers kore nahi nare dabar 3 prime numbers agar hai.
    Udaharan
    Is_multiply_prime(400) == True, 4 is prime"""
    """Dengan kok sama saya dapat sekalik agar yaa nare 3 * 5 + 5 * 3 atau 5 * (2 + 1) = 7 * 3"""
    if a > 100:
        return False
    else:
        #2 * 3 = 3
        b = 3
        while b * b <= a:
            if a % b == 0:
                return False
            b += 1
        return True
