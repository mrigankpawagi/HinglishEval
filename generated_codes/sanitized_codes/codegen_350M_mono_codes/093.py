
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
    encoded = ''
    message = message.lower()
    count=0
    for letter in message:
       if letter in ENGLISH_ALPHABET:
           encoded += ENGLISH_ALPHABET[(ENGLISH_ALPHABET.index(letter)-2)*2]
        if letter in VOWELS:
            encoded += VOWELS[count]
        count += 1
    return encoded