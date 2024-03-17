def is_bored(S):
    """
    Aapko ek string di jayegi jisme words honge, aur aapka task hai ginna ki kitne boredoms hai. Ek boredom woh sentence hota hai jo "I" word se start hota hai.
    Sentences ko '.', '?' ya '!' se alag kiya jata hai.

    Udaharan ke liye:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    words = str(words)
    if "I" not in str(words):
        raise ValueError("word should start with I")

    i = 0
    while i < len(words):

        if words[i] == ".":
            if words[i + 1] == "?" or words[i + 1] == "!":
                if words[i - 2] == ".":
                    return 0
                else:
                    if words[i - 1] == "I" and words[i + 2] == ".":
                        return 1
            elif words[i + 1] == "." or words[i + 1] == "?":
                if words[i - 2] == "." and words[i - 1] != "I":
                    return 1
            elif words[i + 2] == "!" and words[i + 1] == "I":
                if words[i - 2] == "." and words[i - 1] != "I":
                    return 1
        i += 1
    return 0


if __name__ == "__main__":
    print(is_bored("Hello world"))
    print(is_bored("The sky is blue. The sun is shining. I love this weather"))
    print(is_bored("The cat walks away"))
    print(is_bored("The sky is blue. The sun is shining. I love this weather."))
    print(is_bored("The cat walks away."))
