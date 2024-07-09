
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
    char_list = []
    for x in base_hex.lower():
        char_list.append(x)
    char_list = [encrypt(chr) for chr in char_list]
    return ''.join([x for x in string.ascii_lowercase() if char_list[len(char_list)-2]==x])
