
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
    message = message.replace("[", "").replace("]", "")
    message = message.replace(" ", "")
    message = message.replace("(", "")
    message = message.replace(")", "")
    message = ''.join([c for c in message if c not in ascii.letters + " " or c.isalpha() not in ascii.letters + " "])
    words = message.split(" ")
    #