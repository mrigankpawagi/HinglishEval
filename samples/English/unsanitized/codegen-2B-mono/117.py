
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
    words = []

    while(len(s) > 0 and s[:1]!=''):
        if s.lower()[0] not in'qwrtypsdfghjklzxcvbnm':
            temp = s[:len(s)-1]
            s = s[len(s)-1:]
        else:
            temp = s
        for w in temp.split():
            if any(char.lower() not in "qwrtypsdfghjklzxcvbnm" for char in w):
                words.append(w)
        temp = words

    return set(words)
    

# testing
if __name__ == '__main__':
    assert select_words("Mary had a little lamb", 4) == {"little"}
    assert select_words("Mary had a little lamb", 3) == {"Mary", "lamb"}
    assert select_words("simple white space", 2) == []
    assert select_words("Hello world", 4) == {"world"}
    assert select_words("Uncle sam", 3) == {"Uncle"}

    print('done')
