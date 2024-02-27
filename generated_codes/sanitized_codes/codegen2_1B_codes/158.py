
def find_max(words):
    """
    Ek function likho jo strings ki list ko accept karta hai.
    List mein alag alag shabd hote hain. Unique characters ki maximum number wala shabd return karo. Agar multiple strings mein maximum number of unique characters ho, toh lexicographical order mein sabse pehle aane wala shabd return karo.
    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb","cc"]) == "aaaaaaa"
    """
    word_words = set(words)
    max_id = words[0]
    max_string_id = words[0]
    for i in range(1, len(words)):
        if words[i] not in word_words:
            if words[i] > max_id and words[i] not in max_string_id:
                max_string_id = words[i]
                max_id = max_string_id
                return max_string_id
        elif words[i] == max_id and words[i] in word_words and i not in max_string_id:
            max_id = words[i]
            max_string_id = words[i]
    return max_id