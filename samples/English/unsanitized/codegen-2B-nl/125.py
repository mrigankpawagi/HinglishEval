
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
    iwsp = 0
    list = []
    for word in txt.lower():
        for i in range(len(word)):
            char = ord(word[i])
            if char in range(ord('a'), ord('z')):
                #odd order or no even order
                if i % 2 == 0:
                    list.append(word[i:i+1])
                else:
                    #add whitespaces or comma in front
                    iwsp += (ord('a') - ord('a') % len(word) - 1) % len(word) 
                    list.append(''* (iwsp if iwsp > 0 else 0)) + word[i:i+1] + " "
            #even order
           