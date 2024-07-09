

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
    lower_vowels = {'a', 'e', 'i', 'o', 'u'}
    clean_text = []
    for char in text:
        if char.casefold() in lower_vowels:
            clean_text.append(char)
    return ''.join(clean_text)


if __name__ == '__main__':
    import doctest

    result = doctest.docfile_html(__file__)
    print(result)

    # Test 1: The script prints test output to the shell properly.
    print(remove_vowels('This is a test!'))
    print(remove_vowels('This is a test!'))

    # Test 2: Test 2 adds 'a' on the last vowel.
    print(remove_vowels('Zed, I saw Zee!'))
