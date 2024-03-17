
def histogram(test):
    """
    Ek string di gayi hai jo space separated lowercase letters ko represent karti hai, return karo ek dictionary
    jisme sabse zyada repeat hone wale letter aur unke corresponding count ho.
    Agar kai letters ka occurrence same hai, to un sabhi ko return karo.
    
    Udaharan:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}
    """

    print('\tUdaharan:')
    print()
    hist = {}  # empty dictionary
    
    for i, s in enumerate(test):
        s = s.lower()
        for x, y in zip(s, s[1:]):
            hist[x] = hist.get((x, None), 0) + 1 if y == x else 0

    return hist
