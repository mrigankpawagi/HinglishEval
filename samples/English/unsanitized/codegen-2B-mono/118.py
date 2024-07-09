
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    vowels = "aeiou"
    word = word.lower()
    new_word = ""

    for i in range(0, len(word)):
        if word[i] not in vowels:
            new_word = new_word + word[i]

    vowel_index = 0
    if new_word!= word:
        vowel_index = new_word.find("a")
        vowel_index += 2

    return word[0:vowel_index]

# Test
assert get_closest_vowel("yogurt") == "u"
assert get_closest_vowel("FULL") == "U"
assert get_closest_vowel("quick") == ""
assert get_closest_vowel("ab") == ""
