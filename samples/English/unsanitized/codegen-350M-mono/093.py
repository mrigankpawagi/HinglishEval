
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
    # Encodes to lower-case and replace punctuation
    message = message.lower().translate(None, '".?!*;:;|&')
    # Replaces single letters and multiple spaces
    message = message.replace(' ', '').replace('.', '. ')
    # Replaces uppercase letters and single spaces with an uppercase letter
    message = message.replace('e', 'e').replace('o', 'o').replace(' ','.').replace('-','.')
    # Replaces uppercase letters with 2 more places from the upper
    message = message.replace('A', 'a').replace('e', 'e').\
        replace('O', 'o').replace('O', 'i').replace(' ','.').\
        replace('I', 'a').replace('g','g').replace('s','s').replace('S','S')
    punctuation = ''.join(message)
    # Splits punctuation on each character, and adds in the letter with the first occurence
    # in the text as the new capitalized letter
    punctuation_split = punctuation.split()
    cleaned_message = tuple(''.join(x) for x in itertools.groupby(punctuation_split[:-1]))
    # Replaces non alphabetic characters with lower_cased versions.
    cleaned_message = dict((re.sub(r'[^a-z]', '', u, flags=re.I), c) for [u, c] in cleaned_message)
    # Replaces all other characters from each letter with the letter the letter
    # appears in the position indicated by the letter's position.
    cleaned