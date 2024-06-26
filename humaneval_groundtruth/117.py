
def select_words(s: str, n: int):
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
    assert isinstance(s, str), "invalid inputs" # $_CONTRACT_$
    assert all(ch == " " or ch.isalpha() for ch in s), "invalid inputs" # $_CONTRACT_$
    assert type(n) == int, "invalid inputs" # $_CONTRACT_$
    assert n >= 0, "invalid inputs" # $_CONTRACT_$

    ans = []
    for word in s.split(" "):
        if word != "":
            c_cnt = len(list(filter(lambda ch: ch not in "aeiouAEIOU", word)))
            if c_cnt == n: ans.append(word)
    return ans

def check(candidate):

    # Check some simple cases
    assert candidate("Mary had a little lamb", 4) == ["little"]
    assert candidate("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert candidate("simple white space", 2) == []     
    assert candidate("Hello world", 4) == ["world"]
    assert candidate("Uncle sam", 3) == ["Uncle"]


    # Check some edge cases that are easy to work out by hand.
    assert candidate("", 4) == []
    assert candidate("a b c d e f", 1) == ["b", "c", "d", "f"]


check(select_words)