
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello!!!Wdlor'
    """
    res = []
    for word in s.split():
        lower = word.lower()
        val = ord(lower)
        res.append(lower)
        #res.append(chr(order[val])[:] - val + val)

    res = ''.join(res)

    #res = word.capitalize()  
    if len(res) < len(s):
        res = res[:len(s)]
        for i in range(len(s), len(res)-1, -1):
            tmp = res
            # if i == len(s):
            #     break
            # t = ord(chr(ord(tmp) - 1)) + 1
            if ord(res[i]) <= ord(res[i-1]):
                res = res[:i-1] + res[i:]
            else:
                tmp = res[i:] + res[:i]
                res = res[:i-1] + tmp[:]
    '''
    res = []
    for word in s.split():
        lower = word.lower()
        val = ord(lower)
        res.append(chr(order[val])[:] - val + val)
    res = ''.join(res)
    return res
'''
