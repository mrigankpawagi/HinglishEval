def find_max(words):
    """
    Ek function likho jo strings ki list ko accept karta hai.
    List mein alag alag shabd hote hain. Unique characters ki maximum number wala shabd return karo. Agar multiple strings mein maximum number of unique characters ho, toh lexicographical order mein sabse pehle aane wala shabd return karo.
    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb","cc"]) == "aaaaaaa"
    """
    if len(words) <= 1:
        return words[0]
    else:
        count = {}
        max = -1111
        for word in words:
            char_set = set(word)
            if len(char_set) > max:
                max = len(char_set)
            count[len(char_set)] = count.get(len(char_set), 0) + 1
        return words[count[max].index(max)]