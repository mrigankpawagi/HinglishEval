

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
    text = text.replace(',', 'a')
    for vowel in text.lower():
        if vowel in 'vowel': continue
        if 'vowel' not in vowels: continue
        if vowel in 'kvijklm': continue
        if vowel in 'ababab': continue
        if vowel in 'bcdf': continue
        if vowel in 'jm\n': continue
        if vowel in '\n': continue

    # print(text)
    for vow in vowels:
        if vowel in vow: continue
        if vowel not in vow: continue
        if vowel not in 'ababab' or vowel not in vowels: continue

    # remove vowel
    remove_vowels(text)
