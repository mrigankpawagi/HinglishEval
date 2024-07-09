
def find_max(words):
    """
    Ek function likho jo strings ki list ko accept karta hai.
    List mein alag alag shabd hote hain. Unique characters ki maximum number wala shabd return karo. Agar multiple strings mein maximum number of unique characters ho, toh lexicographical order mein sabse pehle aane wala shabd return karo.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """    unique_chars = []
    for x in words:
        for c in x:
            if c not in unique_chars:
                unique_chars.append(c)

    unique_chars.sort(key=str.lower)
    
    #unique_chars += ["and","or","if","for","than","so","the","by","at","not","on","and","the","of","be","we","as","of","you","an","and"]
    if len(unique_chars)>0:
        return unique_chars[0]
    else:
        return None
    
