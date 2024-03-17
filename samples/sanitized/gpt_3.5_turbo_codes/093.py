def encode(message):
    """
    Ek function likho jo ek message leta hai, aur usko aise encode karta hai
    ki wo saare letters ki case ko swap kar deta hai, saare vowels ko
    unke aage wale 2nd letter se replace kar deta hai english alphabet mein.
    Sirf letters maan lo.
    Udaharan:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encoded_message += char.upper()
            else:
                encoded_message += char.lower()
            if char.lower() in ["a", "e", "i", "o", "u"]:
                encoded_message += chr(ord(char) + 2)
        else:
            encoded_message += char
    return encoded_message
