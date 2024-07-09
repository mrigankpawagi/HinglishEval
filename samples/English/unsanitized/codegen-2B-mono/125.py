
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1,... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    res = []
    i = 0
    j = 1
    words = txt.split()
    for word in words:
        res.append(word)
        if j%2 == 0:
            res[i] = res[i] + " " + word
        j += 1
        i += 1
    
    return res 
    
