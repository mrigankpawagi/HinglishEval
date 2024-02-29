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
    # Your code here
    if len(string) == 1:
        return True
    if string[0] == "0":
        return False
    if string[0] == "1":
        return True
    if string[0] == "2":
        return True
    if string[0] == "3":
        return True
    if string[0] == "5":
        return True
    if string[0] == "7":
        return True
    if string[0] == "9":
        return True
    return False
