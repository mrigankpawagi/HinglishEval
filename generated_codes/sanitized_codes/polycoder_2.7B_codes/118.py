
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
    lpos = len(word) - 1
    maxD = 0.75 * len(word)
    i, count = 1, 0
    while i <= maxD and count < 3:
        if word[lpos - 1] == word[lpos]:
            count += 1
        i += 1
    if count <= 2:
        return word
    if count == 3:
        return "aeiou"
    elif count > 3:
        return "fa"
    else:
        i = max(i - 1, 0)
        if word[2 * lpos - 1] == word[2 * lpos - i]:
            count = 2
        else:
     