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
    return "".join(c for c in text if c not in "aeiou")