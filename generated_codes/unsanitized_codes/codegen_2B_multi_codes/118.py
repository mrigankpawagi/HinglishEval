
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
    # First we need to count consonants from the right side of the word.
    result = 0
    count = 0
    for i in range(len(word)-1, -1, -1):
        if word[i].isupper():
            count += 1
    for i in range(len(word)-1, -1, -1):
        if word[i].isupper() and word[i-1]!= 'a':
            result += 1
            if word[i-1].lower() == "e" or word[i-1].lower() == "i" or \
                    word[i-1].lower() == "o" or word[i-1].lower() == "u":
                break
    return word[-count-result:]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
