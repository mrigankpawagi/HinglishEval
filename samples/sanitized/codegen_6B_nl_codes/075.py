def is_multiply_prime(a):
    """
    Ek function likho jo true return kare agar diya gaya number 3 prime numbers ka multiplication hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai.
    Udaharan:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if len(range(2, 21)) == 0:
        return False
    if sieve_function(a) == False:
        return False
    sieve_array = []
    for i in range(len(a) - 1, -1, -1):
        while (i + 1) < len(a):
            if i + 1 >= len(a):
                sieve_array.append(True)
                continue
            if a[i] // a[i + 1] == 0:
                sieve_array.append(False)
                break
    if min(sieve_array) == True:
        return True
    else:
        return False