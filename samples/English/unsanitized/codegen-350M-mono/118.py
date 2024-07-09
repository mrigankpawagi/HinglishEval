
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
    word = word.split()
    num = 1
    vowel_list = ["a","e","i","o","u"]
    max = 0
    max_num = -1
    for i in range(len(word)):
        if (word[i-num] in vowel_list and word[i+num] in vowel_list):
            min = abs(vowel_list.index(word[i-num]) - vowel_list.index(word[i+num]) )
            number = vowel_list.index( word[i-num] )
            num+=1
            num += vowel_list.index(word[i+num])

            d = abs( number - num )

            if d > max:
                max = d
                max_num = number
                min_num = num
    return max_num
