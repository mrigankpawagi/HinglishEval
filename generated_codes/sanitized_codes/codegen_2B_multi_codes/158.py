
def find_max(words):
    """
    Ek function likho jo strings ki list ko accept karta hai.
    List mein alag alag shabd hote hain. Unique characters ki maximum number wala shabd return karo. Agar multiple strings mein maximum number of unique characters ho, toh lexicographical order mein sabse pehle aane wala shabd return karo.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """   words_arr = list(words)
    if len(words_arr) == 0:
        return ""

    def sort_string(strng):
        return map(chr, map(ord, strng))

    sorted_words = list(map(sort_string, words_arr))
    return sorted_words[len(sorted_words) - 1]
