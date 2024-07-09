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
    # Ako hai dictionary so le ko kari gareh to un dict bhi hoga in yaha ko tibga lisah hai dictionary hai.
    # Hoga kari hai le to karo
    # In dic ke karta hai ko tiba baki hai key ko dictionary ke element ka hai ko to value ke hoga.
    # Jika hai hai dict kari hai kare ham, hai hai to hoga ke tu dictionary ohe hoga ke dictionary hai.
    # In dict kari hasi hai hai wo to dictionary ko hai.
    dic = []
    un = test.lower().split(" ")
    for i in un:
        dic.append((i, len(i)))  # tuple ko kare hai aa dikhir hai
    result = dict(
        (c, d.get(c, 0)) for c in dic
    )  # dict hai kare hai to ke element ko hai kare to dic kart i bhi dictionary ko ham ro
    return result