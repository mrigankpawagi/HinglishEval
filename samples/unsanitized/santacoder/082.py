
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
    # check if string is empty - if true return False
    if not string:
        return False
    
    length = len(string)
    for idx, char in enumerate(string):
        if char.isdigit() or char == '-':
            continue
        if idx == 0 or char!= string[idx-1]:
            if string[idx] == string[idx-1]:
                # loop until char repeating 0 times
                if string[idx:idx+length] == string[idx+1:idx+length]:
                    return True
            else:
                # loop until string without char ek atreve le hooke
                if string[idx:length] == string[idx:idx+length]:
                    return True
    # string length is prime - true return True
    return length == INT_LEN

