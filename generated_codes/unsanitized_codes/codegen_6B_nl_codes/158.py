
def find_max(words):
    """
    Ek function likho jo strings ki list ko accept karta hai.
    List mein alag alag shabd hote hain. Unique characters ki maximum number wala shabd return karo. Agar multiple strings mein maximum number of unique characters ho, toh lexicographical order mein sabse pehle aane wala shabd return karo.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb","cc"]) == "aaaaaaa"
    """
    count = {}

    for word in words:
        count[word]
        if len(word) == 1:
            return word
        for w in count.values():
            if len(word) < len(w):
                return w
    return count[max(set(words))]

Words that I have entered for example are:
array = ["name", "of", "string"]

but max function has returned "of" instead of "string". Is there some problem with the above mentioned code? How can I fix it?

A:

