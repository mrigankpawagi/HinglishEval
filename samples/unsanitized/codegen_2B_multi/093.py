
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



# test
#print encode('test')
#print encode('This is a message')

# python version > 3
try:
    message = "saved to file"
    print encode(message)
except:
    pass

# python version < 3
try:
    message = "saved to file"
    print encode(message)
except:
    print "error"
    sys.exit('ERROR')

if __name__ == "__main__":
    import doctest
    suite = doctest.DocFileSuite(
                    'encoding.txt', clear_globs=False, report=None,
                    optionflags=doctest.ELLIPSIS | doctest.IGNORE_EXCEPTION_DETAIL | doctest.DONT_ACCEPT_BLANKLINE)
    #suite = doctest.master.testfile('encoding.txt')
    suite.run(globs={'encode':encode, 'alphaChars':alphaChars})
