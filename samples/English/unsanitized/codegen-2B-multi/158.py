
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb","cc"]) == ""aaaaaaa"
    """
    unique_chars = [c for c in "".join(words)]
    max_length = len(max(unique_chars))
    return "".join(sorted(words))


if __name__ == "__main__":
    cases = [
        ("a", "aaaa", 1),
        ("bb", "abb", 1),
        ("bbb", "abba", 1),
        ("abb", "bbbb", 2),
        ("abc", "abbb", 2),
        ("ab", "abbb", 3),
        ("aa", "bbb", 3),
        ("abc", "accc", 5),
        ("abbbbbbllll", "aaaaaabbbbbbbllllllll", 5)
    ]

    for i, (x, y, result) in enumerate(cases):
        print(i + 1, x, y)
        if result!= find_max(x.split()):
            print(y)
            break