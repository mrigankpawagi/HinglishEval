
def words_string(s):
    """
    Aapko ek string di jayegi jisme words commas ya spaces se separated honge. Aapka task hai
    string ko words mein split karna aur words ki array return karna.
    
    Jaise ki:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    return s.split()

# 2.
def is_palindrome(s):
    """
    Aapko ek string di jayegi. Aapko check karna hai ki string palindrome hai ya nahi.
    
    Jaise ki:
    is_palindrome("racecar") == True
    is_palindrome("hello") == False
    """
    return s == s[::-1]

# 3.
def is_prime(n):
    """
    Aapko ek integer di jayegi. Aapko check karna hai ki integer prime hai ya nahi.
    
    Jaise ki:
    is_prime(13) == True
    is_prime(14) == False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 4.
def is_leap_year(year):
    """
    Aapko ek integer di jayegi. Aapko check karna hai ki integer leap year hai ya nahi.
    
    Jaise ki:
    is_leap_year(2020) == True
    is_leap_year(2019) == False
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# 5.
def is_leap_year_2(year):
    """
    Aapko ek integer di jayegi. Aapko check karna hai ki integer leap year hai ya nahi.
    
    Jaise ki:
    is_leap_year_2(2020) == True
    is_leap_year_2(2019) == False
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# 6.
def is_leap_year_3(year):
    """
    Aapko ek integer di jayegi. Aapko