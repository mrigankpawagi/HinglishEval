
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
    
    if len(word) == 0:
        return ""
    
    for i in range(len(word)):
        lower = word[i].lower()
        upper = word[i].upper()
        
        print("i", i, "lower", lower, "upper", upper)
        
        if i>0 and last_vowel_position > 0:
            if upper == "Y" or lower == "Y":
                return word[last_vowel_position]   
        
        last_vowel_position = 1 if last_vowel_position == 0 else 0
        
        if upper in vowels and lower not in consonants:
            return upper
        elif upper not in vowels and lower in consonants:
            return lower
        elif lower!= "" and upper not in vowels:
            return lower

    return ""
