
def find_max(words):
    """
    Ek function likho jo strings ki list ko accept karta hai.
    List mein alag alag shabd hote hain. Unique characters ki maximum number wala shabd return karo. Agar multiple strings mein maximum number of unique characters ho, toh lexicographical order mein sabse pehle aane wala shabd return karo.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    words.sort()  # sort karne ke liye
    # print(words)
    # words = list(set(words))  # unique words find
    maximum = ""  # maximum words liye
    # print(words)
    for word in words:
        if len(word) > len(maximum):
            maximum = word  # shabd mein unique words hai
        elif len(word) == len(maximum):
            if word in maximum:
                maximum = word  # maximum se pehle aane wala shabd
            else:
                maximum = maximum
    return maximum


print(find_max(["aaaaaaa", "bb" ,"cc"]))
print(find_max(['game', 'of', 'string']))
