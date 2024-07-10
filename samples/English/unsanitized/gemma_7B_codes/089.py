
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
    result = ""
    for i in s:
        # Code here
        if (i >= "a" and i <= "z"):
            result += chr((ord(i) + 2) % 128)
    return result


def decrypt(s):
    """
    Ek function banaiye decrypt jo ek string ko argument ke roop mein leta hai aur
    ek encrypted string return karta hai jisme alphabet ko rotate kiya gaya hai.
    Alphabet ko aise rotate karna chahiye ki letters 
            do se multiply kiye gaye do places ke neeche shift ho jaye.
            Jaise ki:
            decrypt('lm') returns 'hi'
            decrypt('ewhjklnop') returns 'asdfghjkl'
            decrypt('kj') returns 'gf'
            decrypt('ix') returns 'et'
    """
    result = ""
    for i in s:
        result += chr((ord(i) - 2) % 128)
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().lower())[:]
    for i in range(n):
        s[i], s[n - i - 1] = s[n - i - 1], s[i]
    s = ''.join(s)
    print(encrypt(s))
    print(decrypt(encrypt(s)))
