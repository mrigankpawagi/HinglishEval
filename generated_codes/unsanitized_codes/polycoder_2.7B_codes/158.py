
def find_max(words):
    """
    Ek function likho jo strings ki list ko accept karta hai.
    List mein alag alag shabd hote hain. Unique characters ki maximum number wala shabd return karo. Agar multiple strings mein maximum number of unique characters ho, toh lexicographical order mein sabse pehle aane wala shabd return karo.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """    if not words:
        return ""
    words = list(words)
    res = ""
    for w in words:
        if len(w) > 7:
            continue
        if w[len(w)-1] not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            continue
        if w[-1] == "s":
            continue
        if w[-1] in ["g"]:
            continue
        res += w[:1] + w[-1]
        for i in range(1, len(w) - 1):
            if w[i:i+1] in ["a", "e", "i", "o", "u"]:
                res += w[i - 1] + w[i:i + 1]
    if (
        len(words) > 1
        and words[0] in