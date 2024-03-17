
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
    if not test:
        return {}

    word = test[0]
    result_dict = {}
    char = test[1]
    frequency = 0
    for key in test:
        count = 0
        if key == word:
            if char in result_dict:
                frequency += 1
            else:
                result_dict[char] = 1
                count += 1
        else:
            if char not in result_dict:
                if char == word:
                    result_dict[char] = 1
                else:
               