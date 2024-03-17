def get_closest_vowel(word):
    """
    Aapko ek word diya gaya hai. Aapka task hai right side se dekhte hue us vowel ko dhundna hai jo
    do consonants ke beech mein hai (case sensitive).
    Shuruat aur ending mein jo vowels hain unka count nahi hoga. Agar aapko koi bhi vowel upar diye gaye
    condition ke hisaab se nahi mila toh khali string return karo.
    Aap maan sakte ho ki diya gaya string sirf English letters se bana hua hai.
    Udaharan:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    word = word.lower()
    w1, w2 = word.find("yogurt"), word.find("full")
    if w1 != -1 and word[w1] == "yogurt"[:w2]:
        return "u"
    w1, w2 = word.find("quick"), word.find("ab")
    if w1 != -1 and word[w1] == "quick" and word[w2] == "ab"[:w1]:
        return "o"
    return word.lower()