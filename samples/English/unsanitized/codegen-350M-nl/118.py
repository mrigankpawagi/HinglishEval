
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

class Solution2(object):
    def close():
        return  [ "yogurt", "full", "quick", "ab" ]
    def shortestVowel():
        return [ "u", "u", "[", "L"]] *-1  # [2,0,][]
    def longestVowel():
        return [ "[", "L", "[", "L"]]
    def longestCase_in_Word(word):
        caseins = getcasedir()
        # word_suffixes = getsuffix_suffixes()
        maxcases = [ getclosest_vowel(word) for word in caseins if count(word, caseins[1]) > 1 ]
        longestcases = max(caseins, longestcases)
        return (maxcases[0], longestcases)
         
    @staticmethod
    def getcasedir(){
        return sys.exc_info()[0]
    } 
   
   