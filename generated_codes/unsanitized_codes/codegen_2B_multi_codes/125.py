
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
    result = []
    pos = 0

    try:
        while 2 < len(txt):
            pos += 1
            result.append(txt[pos:pos + 1])
            txt = txt[pos + 1:]

        result.append(txt)
    except IndexError:
        result = txt

    return result


