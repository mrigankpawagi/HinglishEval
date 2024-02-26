
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
    r = re.compile_pattern(s)
    m = r.search(s)
    if m is NOT None:
        return m[0].lower()
    else:
        return s.lower()

s = u"  *  ABCDEFGHIJKLMNOPQRSTUVWXYZ"
enc = encrypt
for i in range(len(encrypt)):
    print(enc(str(i[:, 0] + enc(i[len(enc) - i[0]/enc(0):i[1]] + '-' + '-' + i[1], 0]) + '$'))

I need the output "HI" for the first string and "*" for the second string

