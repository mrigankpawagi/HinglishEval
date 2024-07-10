
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    from collections import defaultdict


def is_unique(val):
    return len({val: (val == 1)}) >= 2


def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    from collections import defaultdict


    lookup = defaultdict(int)
    for word in words:
        lookup[word] += 1
    max_char_count = 0
    max_word = ""

    for word, char_count in lookup.items():
        if char_count > max_char_count and is_unique(word):
            max_char_count = char_count
            max_word = word
    return max_word

if __name__ == '__main__':
    from unittest import TestCase
    import sys
    words = sys.argv[1]
    if len(sys.argv) > 2:
        print "Invalid number to arguments"
        print "Ex: python %s <inputlist>" % (sys.argv[0])
        return


    # words = ["name", "of", "string"]
    # words = ["name", "enam", "game"]
    #words = ["aaaaaaa", "bb", "cc"]
    test = TestCase(name="Test_find_max")

    test.assertEqual(find_max(words), "string")
    test.assertEqual(find_max(["string", "name"]), "string")
    test.assertEqual(find_max(["string", "enam"], "enam"), "enam")
    test.assertEqual(find_max(["aaaaaaa", "bb", "bb"]), "")
    test.assertEqual(find_max(words), "string")
    test.assertEqual(find_max(["name", "enam", "game"], "enam"), "enam")
    test