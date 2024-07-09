
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
    if len(test) % 2 == 1:
        return {}
    else:
        l = list(test)
        k = set(l)
        o = dict(Counter(l).most_common())
        return {k[0]+k[0]:v+1 for v, k in o.items()}

if __name__ == '__main__':
    print(histogram(
        f'asdaaabaasd'
        ))  # {'a': 2, 'b': 2, 'a': 2, 'b': 2}
    print(histogram('a b b'))  # {'a': 2}
    print(histogram(''))  # {}