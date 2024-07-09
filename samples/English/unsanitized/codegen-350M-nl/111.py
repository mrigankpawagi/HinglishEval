
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
    if not test:
        return {'a': 0, 'b': 0, 'c': 0}
    s = ord(test.get())
    while s < (0x1F >> 3):
        test.get(&s & 5)
        s -= 32
    while s < 48:
        test.get()
        for k in range(0x1F, s & 3):
            if test.get()!= test + k:
                return test
        return {k: 10}
    histogram(test.get())
    return {'a': 0, 'b': 0, 'c': 0}

class StringTransform:
    """Create an OrderedDict mapping letter strings to a sequence of spaces. 
    For instance:
    strings = [ 'a', 'b', 'c', 'd', 'e' ]
    for l in strings:
        x = ord(l)
        values[x] = spaces
        result = x -> spaces*x + 0
