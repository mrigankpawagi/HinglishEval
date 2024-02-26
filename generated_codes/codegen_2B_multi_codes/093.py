
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    #This function is a method because it needs to know the 
    #word boundary. 
    message = word_boundary(message)

    #Encode everything and check to make sure we aren't
    #redefining the string in place
    result = encode_word.findall(encode_word_map(message))

    #The below line uses the method of iterlist which will
    #redefine the string so that we can modify the end.
    return result

if __name__ == "__main__":
    encode('This is a message') 
  
    