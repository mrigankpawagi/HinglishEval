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
    if string == "":
        return True
    length = len(string)
    if length % 2 == 0:
        return True
    else:
        return False