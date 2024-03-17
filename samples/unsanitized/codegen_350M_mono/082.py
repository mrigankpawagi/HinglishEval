
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
    result = False
    count = 0
    string = string.lower()
    for character in string:
        if character.isalpha():
            count += 1
    if count == 0:
        return result
    else:
        return True


