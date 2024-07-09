
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
    vowelCounter = {"ae":"a", "ay":"a", "ah":"a", "ao":"a", "aw":"a", "ax":"a", "eh":"e", "ey":"e", "ih":"i", "iy":"i", "oy":"o", "ux":"u",
                    "uu":"u", "ux":"u", "iy":"i", "iy":"y", "uh":"e", "uw":"u", "ix":"x"
    }
    
    wordList = word.split()

    vowelsWordList = []
    for i in wordList:
        for values in vowelCounter.items(): 
            key, value  = values
             
            if i == key:
                vowelsWordList.insert(0, value)

    return "".join(vowelsWordList)

print(get_closest_vowel("yogurt"))
print(get_closest_vowel("FULL"))
print(get_closest_vowel("quick"))
print(get_closest_vowel("ab"))
