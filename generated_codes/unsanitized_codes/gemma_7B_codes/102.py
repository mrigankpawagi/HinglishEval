
def choose_num(x, y):
    """
    Yeh function do positive numbers x aur y leta hai aur return karta hai
    sabse bada even integer jo range [x, y] mein inclusive hai. Agar 
    aisa koi number nahi hai, toh function ko -1 return karna chahiye.

    Jaise ki:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x < 0 or y < 0:
        return -1
    if x > y:
        x, y = y, x
    if x % 2 == 0:
        return x
    else:
        for i in range(x + 1, y + 1):
            if i % 2 == 0:
                return i
        return -1


# 2
def is_prime(n):
    """
    Yeh function do positive integer n leta hai aur return karta hai
    agar n prime hai toh True, aur nahi toh False.

    Jaise ki:
    is_prime(13) = True
    is_prime(14) = False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# 3
def is_palindrome(s):
    """
    Yeh function string s leta hai aur return karta hai
    agar s palindrome hai toh True, aur nahi toh False.

    Jaise ki:
    is_palindrome("racecar") = True
    is_palindrome("race") = False
    """
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


# 4
def is_prime_palindrome(n):
    """
    Yeh function do positive integer n leta hai aur return karta hai
    agar n prime hai aur palindrome hai toh True, aur nahi toh False.

    Jaise ki:
    is_prime_palindrome(13) = True
    is_prime_palindrome(14) = False
    """
    if n < 2:
        return False
    if is_prime(n) and is_palindrome(str(n)):
        return True
    return False


# 5
def is_prime_palindrome_list(n):
    """
    Yeh function list of positive integers n leta hai aur return karta hai
    agar n mein koi bhi prime palindrome hai toh True, aur nahi toh False.

    Jaise