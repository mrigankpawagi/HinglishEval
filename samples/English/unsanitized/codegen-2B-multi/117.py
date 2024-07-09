
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
    if s == None:
        return []
    if n == 0:
        return []
    n = int(n)
    p = {}
    for w in s:
        if p.has_key(w):
            p[w] += 1
        else:
            p[w] = 1
    ret = []
    for x in s.split():
        if p[x] == n:
            ret.append(x)
    return ret
          
# Solution:
# the word list has to be sorted since the longest string is at the beginning
# of the s
# for a given word w
