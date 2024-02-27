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
    str_encryption = "e"
    char_count = len(s)
    string_index = 0
    while char_count > 0:
        value = s[string_index]
        char_index = (value - s[string_index + 1]).bit_length() % 8
        if (8 - char_index) < char_count:
            char_count = char_count - 8 + 8
            char_index += char_count
            j = char_index >> 4
            k = char_index & 0xF
            string_index += 1
            if j >= 48:
                j -= 64
                if j >= k:
                    j -= 48
            elif k >= 50:
                k -= 64