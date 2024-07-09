
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
    if isinstance(string, str):
        return True
    if isinstance(string, basestring):
        return False
    if isinstance(string, int):
        return True
    if isinstance(string, bool):
        return True
    return False


