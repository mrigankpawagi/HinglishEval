
def digitSum(s):
    """
    Task
    Ek function likho jo ek string ko input ke roop mein leta hai aur sirf upper characters'
    ASCII codes ka sum return karta hai.

    Udaharan:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    sum = 0
    for i in s:
        if i.isupper():
            sum += ord(i)
    return sum

# 2
def isPalindrome(s):
    """
    Task
    Ek function likho jo ek string ko input ke roop mein leta hai aur us string ko reverse karke
    original string se compare karke uski palindrome nature check karata hai.

    Udaharan:
        isPalindrome("ab") => False
        isPalindrome("aba") => True
        isPalindrome("abc") => False
        isPalindrome("abccba") => True
        isPalindrome("abccbaA") => False
    """
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False

# 3
def isPrime(n):
    """
    Task
    Ek function likho jo ek integer ko input ke roop mein leta hai aur us integer ko prime number
    check karata hai.

    Udaharan:
        isPrime(1) => False
        isPrime(2) => True
        isPrime(3) => True
        isPrime(4) => False
        isPrime(5) => True
        isPrime(6) => False
    """
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

# 4
def isLeapYear(y):
    """
    Task
    Ek function likho jo ek integer ko input ke roop mein leta hai aur us integer ko leap year
    check karata hai.

    Udaharan:
        isLeapYear(2000) => True
        isLeapYear(2001) => False
        isLeapYear(2004) => True
        isLeapYear(2005) => False
        isLeapYear(2008) => True
        isLeapYear(2009) => False
    """
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0: