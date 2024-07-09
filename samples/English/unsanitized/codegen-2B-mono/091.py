
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    words = S.split()
    boredoms = 0
    for word in words:
        if word[0] == "I":
            boredoms += 1
    if boredoms > 0:
        return bool(boredoms)
    return False

assert is_bored("Hello world") == False
assert is_bored("The sky is blue. The sun is shining. I love this weather") == True

