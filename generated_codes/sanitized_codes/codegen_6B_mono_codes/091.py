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
    i = 0
    count = 0
    if S[0] == "I":
        i = i + 1
    while i < len(S):
        if S[i] == "!" or S[i] == "?" or S[i] == ".":
            i = i + 1
            break
        if S[i] == " ":
            i = i + 1
        else:
            i += 1
    while i < len(S):
        if S[i] == "!" or S[i] == "?" or S[i] == ".":
            break
        if S[i] == " ":
            i = i + 1
        else:
            i += 1
        count += 1
    return count - 1