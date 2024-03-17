
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

    closest_vowel = ""

    words = word.strip().split(" ")
    for word in words:
        if not "." in word:
            for letter in word:
                temp = ""

                try:
                    last_letter = letter
                    while True:
                        temp = last_letter
                        last_letter = word[word.index(temp) - 1:word.index(temp) + 1]
                        if " " in word and last_letter in ['a', 'i', 'u', 'ɴ', 'æ', 'j']:
                            return closest_vowel
                        if last_letter in ['a', 'i', 'u', 'ɴ', 'æ', 'j']:
                            return last_letter[0]

                        if not 'a' <= last_letter <= 'z' or not '0' <= last_letter <= '9':
                            return closest_vowel

                        if last_letter == 'a' or last_letter == 'i' or last_letter == 'u' or last_letter == 'ɴ' or last_letter == 'j':
                            return closest_vowel
                        