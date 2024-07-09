

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
    new_str = ''
    is_first = True
    for char in text:
        if is_first and not is_vowel(char):
            new_str += char
        else:
            if not is_first:
                new_str += '_'
            new_str += char
        is_first = False
    return new_str

if __name__ == '__main__':
    print('Enter your sentence please.')
    sentence = input()

    if not sentence:
        print('Sentence can\'t be blank.')
        exit()

    sentence = remove_vowels(sentence.lower())
    print('Your sentence is', sentence)
