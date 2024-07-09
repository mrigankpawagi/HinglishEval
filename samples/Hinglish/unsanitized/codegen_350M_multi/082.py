
def prime_length(string):
    """
    Ek function likho jo ek string leta hai aur return karta hai True agar string 
    ki length ek prime number hai ya False otherwise
    Udaharan
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    n = len(string)
    a = 2
    if a * n % 2 == 1:
        return False
    if n == 1:
        return True
    return prime_length(string[:n]) and prime_length(string[n:])
