
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    res = []
    txt = txt.split()
    res.extend(txt)
    for i in range(len(txt)):
        if txt[i].isalpha() and (ord(txt[i][len(txt[i]) - 1]) + 1) % 2 != 0:
            res.insert(ord(txt[i][len(txt[i]) - 1]) + 1 - 1, ' ' + txt[i])
    for i in range(len(txt)):
        if txt[i].islower():
            if i < (len(txt) - 1) and txt[i + 1] == ',' or i < (len(txt) - 1) and txt[i + 1] == ' ':
                res.append(txt[i])
            
    return res



print(split_words("Hello,world!") == ["Hello", "world!"])
