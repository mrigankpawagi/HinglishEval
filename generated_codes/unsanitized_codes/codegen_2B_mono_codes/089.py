
def encrypt(s):
    """
    Ek function banaiye encrypt jo ek string ko argument ke roop mein leta hai aur
    ek encrypted string return karta hai jisme alphabet ko rotate kiya gaya ho.
    Alphabet ko aise rotate karna chahiye ki letters 
    do se multiply kiye gaye do places ke neeche shift ho jaye.
    Jaise ki:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    
    # This string to store alphabet 
    # you want to encrypt.
    s_cipher = '' 
      
    # Do loop of encryption 
    for ch in s: 
        # Encryption table will have all  
        # the lowercase alphabets 
        # and it will be in order. 
        # Therefore, index of the element 
        # in the string is equivalent 
        # directly to the index in the 
        # above table. 
        s_cipher = s_cipher + encrypt_table[ord(ch) - ord('a')] 
      
    return s_cipher


