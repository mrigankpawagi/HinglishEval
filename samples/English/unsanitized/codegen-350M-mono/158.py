
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb","cc"]) == ""aaaaaaa"
    """
    a = Counter(["name", "of", "string"])
    dict = {}

    if len(a) in dict:
        a.clear()

    for i, value in a.items():
        a[i] = max(dict[i], value)

    i = 0
    for i, value in sorted(a.items()):
        if i not in dict:
            dict[i] = a[i]
        elif dict[i]!= a[i]:
            dict[i] = True
            dict[i] = a[i]
            i += 1
            i = i % len(dict)

    for i in dict:
        if dict[i] == True:
            return dict[i]


print(find_max(["name", "of", "string"]))
