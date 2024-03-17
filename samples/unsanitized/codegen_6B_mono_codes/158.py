
def find_max(words):
    """
    Ek function likho jo strings ki list ko accept karta hai.
    List mein alag alag shabd hote hain. Unique characters ki maximum number wala shabd return karo. Agar multiple strings mein maximum number of unique characters ho, toh lexicographical order mein sabse pehle aane wala shabd return karo.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb","cc"]) == "aaaaaaa"
    """
    max_len = 0
    max_word = ''
    for word in words:
        l = len(word)
        if l > max_len:
            max_len = l
            max_word = word
    return max_word

