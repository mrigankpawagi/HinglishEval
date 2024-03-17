
def find_max(words):
    """
    Ek function likho jo strings ki list ko accept karta hai.
    List mein alag alag shabd hote hain. Unique characters ki maximum number wala shabd return karo. Agar multiple strings mein maximum number of unique characters ho, toh lexicographical order mein sabse pehle aane wala shabd return karo.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """    if not words:
        return []

    max_id = 0
    nwords = 0
    n = 0
    i = 0
    j = 0
    for word in words:
        try:
            if word == ">":
                i += 1
            elif word == ">=":
                i -= 1
            if word == "<" and i < 0:
                j += 1 + int(word)
            else:
                n += 1
        except ValueError:
            pass

        if j >= i:
            max_id = max(max_id, nwords)
            nwords = n
        else:
            j -= 1

    return max_