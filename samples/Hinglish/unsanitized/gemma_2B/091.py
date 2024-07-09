def is_bored(S):
    """
    Aapko ek string di jayegi jisme words honge, aur aapka task hai ginna ki kitne boredoms hai. Ek boredom woh sentence hota hai jo "I" word se start hota hai.
    Sentences ko '.' , '?' ya '!' se alag kiya jata hai.

    Udaharan ke liye:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    # Your code here
    count = 0
    for i in range(len(S)):
        if S[i] == "I":
            if S[i + 1] == " ":
                count += 1
    return count
