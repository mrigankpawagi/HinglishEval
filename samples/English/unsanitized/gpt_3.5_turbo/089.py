def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    encrypted = ""
    for char in s:
        if char.isalpha():
            ascii_val = ord(char)
            shifted_val = ascii_val + (2 * 2)
            if char.isupper():
                if shifted_val > ord('Z'):
                    shifted_val = shifted_val - 26
            else:
                if shifted_val > ord('z'):
                    shifted_val = shifted_val - 26
            encrypted += chr(shifted_val)
        else:
            encrypted += char
    return encrypted