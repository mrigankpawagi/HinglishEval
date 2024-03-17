
def split_words(txt):
    """
    Ek string di gayi hai jisme words hain, aapko ek list return karni hai jisme words whitespace par split ho. Agar text me koi whitespace nahi hai toh aapko commas ',' par split karna hai. Agar koi comma bhi nahi hai toh aapko alphabet me odd order wale lower-case letters ki count return karni hai, jaise ki ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Udaharan
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3
    """
    if txt.count(" ") == 0:
        if txt.count(",") == 0:
            return sum(ord(i) for i in txt if ord(i) % 2 == 1)
        else:
            return txt.split(",")
    else:
        return txt.split(" ")


# 2
def is_prime(n):
    """
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    Udaharan
    is_prime(1) ➞ False
    is_prime(2) ➞ True
    is_prime(3) ➞ True
    is_prime(4) ➞ False
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# 3
def is_palindrome(txt):
    """
    A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.
    Udaharan
    is_palindrome("racecar") ➞ True
    is_palindrome("race") ➞ False
    is_palindrome("12321") ➞ True
    """
    return txt == txt[::-1]


# 4
def is_leap_year(year):
    """
    A leap year is a year that is divisible by 4, but not by 100, unless it is also divisible by 400.
    Udaharan
    is_leap_year(2000) ➞ True
    is_leap_year(2001) ➞ False
    is_leap_year(1900) ➞ False
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# 5
def is_leap_year_2(year):
    """
    A leap year is a year that is divisible by 4, but not by 100, unless it is also divisible by 400.
    Udaharan
    is_leap_year(2000) ➞ True