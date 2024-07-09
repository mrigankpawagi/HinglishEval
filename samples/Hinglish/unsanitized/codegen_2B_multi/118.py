
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

    vowel_list = ["A", "H", "W", "Y", "J", "D", "Y", "r", "t", "D"]
    return str(vowels_in_str(word))[-1] if word else ""


if __name__ == "__main__":
    print get_closest_vowel("yogurt")
    print get_closest_vowel("FULL")
    print get_closest_vowel("quick")
    print get_closest_vowel("ab")
