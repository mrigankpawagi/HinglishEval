
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb","cc"]) == ""aaaaaaa"
    """
    words = list(words)
    words.sort()
    maxx = ''
    i = 1
    while i < len(words):
        if words[i] == maxx:
            i+=1
            continue
        if not i == 0 and words[i-1] + words[i] in words:
            maxx = words[i-1] + words[i]
            i+=1
            continue
        maxx = words[i]
        i+=1
    return maxx
#find_max([])
#find_max(["name", "enam", "game"])
#find_max(["aaa", "bb", "cc"])
import unittest
class TestExample(unittest.TestCase):
    def test_finding(self):
        self.assertEqual(find_max(['abcdef', 'adef']), 'adef')
    def test_empty(self):
        self.assertEqual(find_max(['']), '')

if __name__ == '__main__':
    unittest.main()
