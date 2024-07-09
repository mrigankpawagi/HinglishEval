
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
    message = message.upper()
    newmessage = []
    vowels = {'A', 'E', 'I', 'O', 'U'}
    for char in message:
        if char.isalpha():
            newmessage.append(encode_letter(char))
        elif char in vowels:
            newmessage.append(encode_letter(char) + char_switch[1])
        else:
            print('Sorry! I only understand letters and vowels.')
            break
    newmessage = ''.join(newmessage)
    return newmessage
