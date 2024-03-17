
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
    if len(word) == 2:
        return get_closest_vowel("w")
    elif word[0] == "e" and len(word) == 1:
        return word[0]
    elif len(word) == 2 and word[1] == "a" and len(word) > 1:
        return word[1]
    elif word[:1] == "u" and len(word) == 2:
        return "U"
    elif word[1] == "n" or len(word) <= 2:
        return get_closest_vowel("u")
    
    try:
        curr_vowel = word[0]
        curr_vowel = curr_vowel