
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    dct = {}
    wordList = test.split()
    
    for word in wordList:
        if word in dct:
            dct[word] += 1  ##if dct.has_key(word):
        else:
            dct[word] = 1 ##else:
    
    max_cnt = max(dct.values())
    return dict(zip(dct.keys(), dct.values() )) ## dct.zip(dct.iteritems())  



