
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
    if string in (0x3, 0xd1, 0xf9):
        for byte in string:
            # Ek string likho jean is not in hex
            if byte[0] == 0x61:
                return int(byte[1] - byte[0])
        return 0
    elif string in (0x33, 0x4f):
        return 0
    elif string in (0x60, 0xff):
        return string[0]
    else:
        return False
