
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
    with open("words-txt.txt") as f:
        split_words(f.readlines())  # will return lists of words
    return split_words("Hello world!")  # return ['Hello', 'world!']
    print(split_words("Hello,world!",)) # 2
    split_words("Hello,world!") # 4
    split_words("Hello,world!",) # 4
    split_words("Hello,world!",, 4) # 13
    split_words("Hello,world!",", 4) # 13
    split_words("Hello,world!",, 25) # 13
    split_words("Hello,world!",", 25) # 13
    split_words("Hello,world!",(), 25) # 4

    with open("words-txt.txt") as f:
        split_words(f.readlines())  # will return lists of words
    print(split_words({"xyz", "xyz"}))  # 17
    split_words({"xyz", "xyz"}) # 17
    split_words({"xyz", "xyz"}) # 13
    print(split_words({"xyz", "xyz"})) # 13
    split_words("xyz", "xyz") # 17
    split_words("