
def is_multiply_prime(a):
    """
    Ek function likho jo true return kare agar diya gaya number 3 prime numbers ka multiplication hai
    aur false agar aisa nahi hai.
    Jahan (a) 100 se kam hai. 
    Udaharan:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    number_dividable = [2,3,5]
    if a in number_dividable:
        return True
    elif a % 2 == 0 :
        return False

    while a > 2:
        a = a - 2
    return True



def solve():
    i = is_multiply_prime

    print(is_multiply_prime(30))
    # return i
solve()
