
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb","cc"]) == ""aaaaaaa"
    """
    for word in words:
        try:
            # If there are multiple results, do the next one.
            if len(words) > 1:
                lst = [m[m.index(n) for n in dict(find_max(w))]
                        for m in m ]
                words=sorted(list(lst),key=lambda k: find_max(words[k]))
        except KeyError:
            pass # There should not be more words.
        c = dict(find_max(words[word]))
        try:
            return c[word]
        except KeyError:
            return None
    return ""  # "None"

