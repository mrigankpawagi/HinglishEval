
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
    message = message.strip()

    letters = sorted(message)
    encoded = ''
    for letter in letters:
        if letter.isalpha():
            encoded += alphaChars.get(letter, '')
        else:
            encoded += letter
    return encoded


