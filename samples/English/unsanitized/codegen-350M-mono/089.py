
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
    result = ''
    for char in s:
        result += chr((ord(char) + 26 - ord('a') - 2) % 26 - ord('a'))
    return result

# def encrypt_letter(letter, alphabet, new_text):
#     """encrypt a single letter. 
#     Assume the text is a string of all ASCII characters plus the code
#     that will be used in alphabet and new_text. 
#     The return value is the encrypted string."""
#     letter = alphabet[letter]
#     print("Encrypting letter '" + letter + "' with \
#         order: " + str(alphabet.index(letter)+1))
#     new_text += letter +''
#     print("Encrypting letter '" + letter + "' with \
#         order: " + str(alphabet.index(letter) + 1))
#     
#     if alphabet.index(letter) == len(alphabet)-1:
#         new_text = new_text[:len(new_text)-1] + chr(ord('*')+alphabet.index(letter) +1) + new_text[len(new_text)-1:]
#         print("Encrypted text: " + new_text)
#         return(new_text)
#     else:
#         new_text = new_text[:len(new_text)-1] + chr(ord('*') + alphabet.index(letter) + 1) + new_text[len(new_text) - 1:]
#         print("Encrypted text: " + new_text)
#         alphabet[alphabet.index(letter