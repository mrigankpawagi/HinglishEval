def encrypt(s):
    encrypted_string = ""
    for char in s:
        if char.isalpha():
            if char.isupper():
                encrypted_string += chr((ord(char) - 65 + 2) % 26 + 65)
            else:
                encrypted_string += chr((ord(char) - 97 + 2) % 26 + 97)
        else:
            encrypted_string += char
    return encrypted_string
