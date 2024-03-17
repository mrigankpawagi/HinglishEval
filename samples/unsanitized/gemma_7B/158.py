def find_max(words):
    """
    Ek function likho jo strings ki list ko accept karta hai.
    List mein alag alag shabd hote hain. Unique characters ki maximum number wala shabd return karo. Agar multiple strings mein maximum number of unique characters ho, toh lexicographical order mein sabse pehle aane wala shabd return karo.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    max_count = 0
    max_word = ""
    for word in words:
        count = 0
        for char in word:
            if char not in word[: word.index(char)]:
                count += 1
        if count > max_count:
            max_count = count
            max_word = word
        elif count == max_count:
            if word < max_word:
                max_word = word
    return max_word
