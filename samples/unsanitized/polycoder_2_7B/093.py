
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
    try:
        alphabet = alphabet_dict[os.path.basename(message).split('.')[0]]
    except IndexError:
        alphabet = ''
    if alphabet == '':
        alphabet = 'a'
    return ''.join(
            [alphabet.upper(),
             '_' +
             [char for char in message if ord(char) < 128]
             ]
           for message in (message.rsplit('! ')[0], message.rsplit('@ ')[-1])
           if message[0] in alphabet)