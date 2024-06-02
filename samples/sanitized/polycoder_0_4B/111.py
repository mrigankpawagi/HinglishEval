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

    _ = test["sabhi"]
    _ = test["karo"]
    _ = test["kasme"]

    result = {}
    for word in test["words"]:

        if word.lower().startswith("katau"):
            key = word.lower().replace("i", "")

            if key not in result:
                result[key] = dict(value=[word] * len(test["words"]))

        else:
            result[word] = dict(value=1)

    return result