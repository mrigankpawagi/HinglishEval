
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
    
    if s:
        words = s.split()
    else:
        return []

    if n < 1:
        return words

    index = 0
    for word in words:
        if len(word) == n:
            yield word
        else:
            index += 1
            cnt = 0
            for x in range(len(word)):
                if not word[x].isdigit():
                    cnt += 1
                    if cnt == n:
                        yield word[:x]
                        break


from time import time
tStart = time()

print len(''.join(select_words('I have a little lamb', 3)))

tEnd = time()

print tEnd-tStart
