
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
    vowels = ["U", "UW", "UH", "AY", "AH", "HH", "B", "D", "DW", "F", "FW", "G", "GY", "J", "KH", "P", "Q", "R", "S", "SH", "T", "TH", "V", "W", "Y", "Z"]
    i = len(word) - 1
    while i >= 0:
        # The index of the first occurent consonant from the right
        while i >= 0 and word[i] not in vowels and (word[i]!= 'B' or i > 2):
            i -= 1
        # The index of the first occurent consonant from the left
        while i >= 0 and word[i] not in vowels and (word[i]!= 'b' or i < 1):
            i -= 1
        if i >= 0:
            break
    return word[i + 1:] if i >= 0 else ""


# The following test case is from the LeetCode's sample.
t = int (input())
for ti in xrange(t):
    r = input()
    s = input()
    print get_closest_vowel(s)
