
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
    # for letter in s:
    #     if int(letter) > 128:
    #         return s
    for letter in s:
        if letter in s:
            break
        else:
            pass
    # return s

    # encrypted_letters = []
    # for j in range(len(s) - 1, -1, -1):
    #     encrypted_letters.append(s[j] ^ s[j + 1])
    # return ''.join(encrypted_letters)

    # return ''.join((str(ord(c) ^ ord(c + 1))) for c in s)

print(a,b)
print(b,c)
print(a,x,y,z,a,z)
#print(x,a,z,y,b,z,a,b,x,y)+'\n'+\
#                 print(a,x,y,z,a,z,b,z,a,b)+'+\n'+
#                 print(''.join((str(