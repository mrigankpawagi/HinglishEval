

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
    from itertools import product, islice
    from itertools import islice
    for i in product(islice(text,0,0),islice(text,1,2)):
        if i[0] in ('A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','i','J','k','L','m','N','o','P','r','S','t','U','v','W','y','A'):
            yield i[1:]
    

