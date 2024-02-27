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
    result = {}
    hyphen = "-" if "-" in test else ""
    test = test.upper()
    test = test.split()
    test_length = [len(x) for x in test]
    test = "\n".join([x if x != "" else "" for x in test])
    test_string = test.split()
    test_string = test_string[hyphen.find(" ") + 1 :]
    for test_name in test_string:
        if test_name[0] == "#":
            continue
        if isinstance(test_name, bytes):
            for x in test_name:
                if x not in (".", '"', "'"):
                    continue
                for c, idx in enumerate(test_string[0:]):
                    new_idx = len(test_string[0:]) + idx if idx == "0" else idx
                    test
