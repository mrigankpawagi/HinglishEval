
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
    letters = alphabet
    res = []
    for v in letters:
        t = 0
        for i in range (len(word)-1, -1, -1):
            if word[i] != v:
                t += 1
            if t == 1:
                res.append(word[i])
    if len(res) != 0:
        res.append(word[0])  
    return res
    

        



assert get_closest_vowel("yogurt")== u



letters = "abcdefghijklmnopqrstuvwxyz"


a = "abcde"

# assert letters.index('b') == letters.index('d')


def alphabet():
    """
    Function to return a list of letters of the alphabet
    
    """
    return [a[i:i+1] for i in range(len(a))]
