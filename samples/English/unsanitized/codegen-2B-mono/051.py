

def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
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
    if not text:
        return text
    else:
        vowels = 'aeiou'
        new_text = []
        for index in range(0, len(text)):
            if text[index] not in vowels:
                new_text.append(text[index])
        return ''.join(new_text)
# This is not the correct code solution, the correct code requires:
            if text[index] in vowels:
                return ''.join(new_text)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
