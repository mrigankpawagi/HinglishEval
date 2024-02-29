

def remove_vowels(text):
    """
    remove_vowels ek function hai jo string leta hai aur vowels ke bina string return karta hai.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = 'aeiou'
    new_text = ''
    for char in text:
        if char not in vowels:
            new_text += char
    return new_text

def remove_vowels_2(text):
    """
    remove_vowels ek function hai jo string leta hai aur vowels ke bina string return karta hai.
    >>> remove_vowels_2('')
    ''
    >>> remove_vowels_2("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels_2('abcdef')
    'bcdf'
    >>> remove_vowels_2('aaaaa')
    ''
    >>> remove_vowels_2('aaBAA')
    'B'
    >>> remove_vowels_2('zbcd')
    'zbcd'
    """
    vowels = 'aeiou'
    new_text = ''
    for char in text:
        if char not in vowels:
            new_text += char
    return new_text

def remove_vowels_3(text):
    """
    remove_vowels ek function hai jo string leta hai aur vowels ke bina string return karta hai.
    >>> remove_vowels_3('')
    ''
    >>> remove_vowels_3("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels_3('abcdef')
    'bcdf'
    >>> remove_vowels_3('aaaaa')
    ''
    >>> remove_vowels_3('aaBAA')
    'B'
    >>> remove_vowels_3('zbcd')
    'zbcd'
    """
    vowels = 'aeiou'
    new_text = ''
    for char in text:
        if char not in vowels:
            new_text += char
    return new_text

def remove_vowels_4(text):
    """
    remove_vowels ek function hai jo string leta hai aur vowels ke bina string return karta hai.
    >>> remove_vowels_4('')
    ''
    >>> remove_vowels_4("abcdef\nghijklm")
    'bcdf\nghjklm'
