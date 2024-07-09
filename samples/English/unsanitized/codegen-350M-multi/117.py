
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    s_word = list()
    if len(s) < 1:
        return s_word
    for x in range(1, len(s)):
        if (len(s[0: x]) == n and s[0: x] == s[1: x + 1]] or (len(s[0: x]) == n and s[0: x] == s[x + 1: len(s)]):
            s_word = s_word + s[x + 1:]
            break
    return s_word

