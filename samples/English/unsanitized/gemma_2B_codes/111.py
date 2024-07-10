
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
    n = {'a':0, 'b':0, 'c' :0}
    i = 0
    while i < len(test):
        test = test[i:i+1]
        if test in n:
            n[test] += 1
        else:
            n[test] = 1
        i += 1
    return n

print histogram("a b c")
