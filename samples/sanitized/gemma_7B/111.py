
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

    # Your code here

    d = {}
    for i in test:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    max_count = 0
    for i in d:
        if d[i] > max_count:
            max_count = d[i]

    res = {}
    for i in d:
        if d[i] == max_count:
            res[i] = d[i]

    return res
