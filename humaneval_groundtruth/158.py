
def find_max(words: list[str]):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    assert type(words) == list, "invalid inputs" # $_CONTRACT_$
    assert all(isinstance(s, str) for s in words), "invalid inputs" # $_CONTRACT_$
    assert len(words) > 0, "invalid inputs" # $_CONTRACT_$

    mx_ch_cnt, ans = 0, ""
    for word in words:
        ch_cnt = len(set(word)) 
        if ch_cnt > mx_ch_cnt or (ch_cnt == mx_ch_cnt and word < ans):
            mx_ch_cnt, ans = ch_cnt, word
    return ans

def check(candidate):

    # Check some simple cases
    assert (candidate(["name", "of", "string"]) == "string")
    assert (candidate(["name", "enam", "game"]) == "enam")
    assert (candidate(["aaaaaaa", "bb", "cc"]) == "aaaaaaa")
    assert (candidate(["abc", "cba"]) == "abc"), 't4'
    assert (candidate(["play", "this", "game", "of","footbott"]) == "footbott")
    assert (candidate(["we", "are", "gonna", "rock"]) == "gonna")
    assert (candidate(["we", "are", "a", "mad", "nation"]) == "nation")
    assert (candidate(["this", "is", "a", "prrk"]) == "this")

    # Check some edge cases that are easy to work out by hand.
    assert (candidate(["b"]) == "b"), 't9'
    assert (candidate(["play", "play", "play"]) == "play")


check(find_max)