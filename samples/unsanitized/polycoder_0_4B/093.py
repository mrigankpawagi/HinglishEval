
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
    import unicodedata
    
    def _encode_unicode(s):
        if s is None:
            return s
        return s.encode(message.name.replace(' ', ''))
    
    result = []
    k = ''
    m = message.name.replace(' ', '')
    
    for i in message:
        if i is None:
            continue
        
        k += i
        m += _encode_unicode(i)
    
    result.append(_encode_unicode(' '.join(k + [''])))
    result.extend(_encode_unicode(' '.join(m)))
    
    
    if six.PY2:
        try:
            result.extend(_encode_unicode(message))
        except UnicodeEncodeError:
            pass
        
    return ''.join(result)

