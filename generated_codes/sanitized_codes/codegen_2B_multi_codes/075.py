
def is_multiply_prime(a):
    """
    Ek function likho jo true return kare agar diya gaya number 3 prime numbers ka multiplication hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai. 
    Udaharan:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """   a_list = list(str(a))
    if a == 1:
        return True
    if len(a_list) > 1:
        for i, j in itertools.izip(itertools.count(), izip(a_list, [0, 1])):
            if i % 2 != 0 and j % 2 != 1:
                return False
    else:
        if is_prime(a_list[0]) == False:
            return False
    return True

