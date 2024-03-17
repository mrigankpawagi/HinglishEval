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
    string = ""
    for i, val in enumerate(message):
        if val.isalpha() and (val[0].lower() == val[0]):
            if val.lower() in vowels:
                string += message[i - 1] + message[i] + " "
                print(string)
    return string[:-1]