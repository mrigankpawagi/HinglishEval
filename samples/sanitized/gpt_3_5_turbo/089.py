def encrypt(s):
    encrypted_string = ""
    for char in s:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + 2) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + 2) % 26 + 97)
            encrypted_string += encrypted_char
        else:
            encrypted_string += char
    return encrypted_string
