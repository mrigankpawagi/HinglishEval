def encrypt(s):
    result = ''
    for char in s:
        if char.isalpha():
            shift = 2 * 2
            char_code = ord(char) + shift
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
            else:
                if char_code > ord('z'):
                    char_code -= 26
            result += chr(char_code)
        else:
            result += char
    return result