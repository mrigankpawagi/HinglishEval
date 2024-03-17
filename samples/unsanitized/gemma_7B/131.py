
def digits(n):
    """
    Ek positive integer n diya gaya hai, odd digits ka product return karo.
    Agar saare digits even hain to 0 return karo.
    Udaharan ke liye:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n == 0:
        return 0
    if n % 2 == 0:
        return 0
    else:
        return n % 10 * digits(n // 10)


# 2
def is_palindrome(n):
    """
    Ek positive integer n diya gaya hai, uske digits ko reverse karke usse n compare karo.
    Agar reverse karke bhi n milta hai to True return karo, warna False.
    Udaharan ke liye:
    is_palindrome(12321) == True
    is_palindrome(12345) == False
    """
    if n == 0:
        return True
    if n % 10 == n // 10:
        return True
    else:
        return False


# 3
def is_prime(n):
    """
    Ek positive integer n diya gaya hai, uske liye prime check karo.
    Agar prime hai to True return karo, warna False.
    Udaharan ke liye:
    is_prime(1) == False
    is_prime(2) == True
    is_prime(3) == True
    is_prime(4) == False
    """
    if n == 0:
        return False
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            return False
    return True


# 4
def is_prime_2(n):
    """
    Ek positive integer n diya gaya hai, uske liye prime check karo.
    Agar prime hai to True return karo, warna False.
    Udaharan ke liye:
    is_prime(1) == False
    is_prime(2) == True
    is_prime(3) == True
    is_prime(4) == False
    """
    if n == 0:
        return False
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    for i in range(3,