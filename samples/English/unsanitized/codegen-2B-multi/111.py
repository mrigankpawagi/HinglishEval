
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
    d = {}  # {char: occurrence}

    if len(test) == 0:
        pass
    elif len(test) == 1:
        if test in d:
            d[test] += 1
        else:
            d[test] = 1
    else:
        curr_char = test[0]
        for letter in test[1:]:
            if letter in d:
                if letter == curr_char:
                    d[letter] += 1
                elif letter in d:
                    d[letter] += d[letter]
            else:
                d[letter] = 1
                
    return d


if __name__ == "__main__":
    for aString in ["abc", "ab ab ab ab", "a", "a a", "a"]:
        print histogram(aString)
