
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
    for vowel_list in vowels_list:
        if word.lower() in vowel_list:
            return vowel_list[0]
    return word.lower()


# def get_closest_vowel2(word):
#   """
#   Aapko kiya task hai string se niche hai. Takhle apko kare hai kar gaya ke usun
#   beech mein string, aare apko takhe hai bina aiha sabt nea hai. 
#   """
#   if get_closest_vowel(word):   # aapko kiya task hai word se niche hai
#     return word[0]
#   else:
#     for key, value in vowels_list.items():
#         if word.lower() in value:
#             return key

# # Get kar and string mein index 0.
# kata = [u'A', u'Z'][ord(char) - ord('A')]
# print(u"Kata ke index 0: ", get_closest_vowel