
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb","cc"]) == ""aaaaaaa"
    """
    maxcount = {}
    for word in words:
        count = len(word)
        if not count in maxcount:
            maxcount[count] = 1
        elif count > maxcount[count]:
            maxcount[count] = count
    return maxcount[:maxcount.get(maxcount.max(), 0)-1]
try:
    from _impkg import *
except ImportError:
    pass
__all__ = ['find_max']
