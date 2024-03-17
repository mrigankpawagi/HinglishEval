
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
    s = s.upper()  # convert to upperCase. 
    s = s.replace(' ', '')  # remove all spaces
    letters = list(s)
    n_letters = []
    i = 0
    j = 0
    n_letters.append(letters[0])
    print_letters = []
    while i < len(letters):
        if i > 75:
            print_letters.append(n_letters[j])
            j += 1
            n_letters.append(letters[i])
            i += 1
        else:
            n_letters.append(letters[i])
            i += 1
    print_letters.append(n_letters[j])
    return ''.join(print_letters)

