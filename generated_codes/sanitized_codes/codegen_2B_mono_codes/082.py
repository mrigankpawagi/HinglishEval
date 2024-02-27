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
    result = True
    for i in range(2, int(len(string))):
        if int(len(string)) % i == 0:
            result = False
            break
    return result