def find_max(words):
    """
    Ek function likho jo strings ki list ko accept karta hai.
    List mein alag alag shabd hote hain. Unique characters ki maximum number wala shabd return karo. Agar multiple strings mein maximum number of unique characters ho, toh lexicographical order mein sabse pehle aane wala shabd return karo.
    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb","cc"]) == "aaaaaaa"
    """
    words[:] = words[:]
    words.reverse()  # find lehe, dhen, oha kele enam, na aenha
    maxed = False  # tome dename
    a = words[0]
    l = len(a)  # number of occurrences of all words
    for s in words:
        if a == s:  # if s and a are equal, find_max dan bb.
            maxed = True
            break
    if maxed == True:
        return a