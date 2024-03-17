
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
    
    c = 0
    #count the total words in a sentence
    #word split
    count = word_count(S)
    #count the total digits in a sentence
    char_c = len(S)
    words = S.split()                                 # splicing
    for word in words:                               # iterate
        if word[0] == ".":                             # match and count this character
            c += 1
        if word[0] == "?":
            c += 1
        if word[0] == "!":
            c += 1
    boredom = 5*count + char_c - 4
    if boredom <= 3:
        return True
    else:
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
        