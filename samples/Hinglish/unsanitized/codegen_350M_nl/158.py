
def find_max(words):
    """
    Ek function likho jo strings ki list ko accept karta hai.
    List mein alag alag shabd hote hain. Unique characters ki maximum number wala shabd return karo. Agar multiple strings mein maximum number of unique characters ho, toh lexicographical order mein sabse pehle aane wala shabd return karo.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb","cc"]) == "aaaaaaa"
    """
    for(c in words):
        c = c.upper()

        if len(c) > max_char_len:
            print("  max character length is", max_char_len)
            return "character is too much"
    return "character is too little"


