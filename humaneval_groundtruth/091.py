
def is_bored(S: str):
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
    assert type(S) == str, "invalid inputs" # $_CONTRACT_$
    sentences = map(lambda x: x.strip(), ((S.replace("?", ".")).replace("!", ".")).split("."))
    return len([s for s in sentences if s.startswith("I ")])
    
def check(candidate):

    # Check some simple cases
    assert candidate("Hello world") == 0
    assert candidate("Is the sky blue?") == 0
    assert candidate("I love It !") == 1
    assert candidate("bIt") == 0
    assert candidate("I feel good today. I will be productive. will kill It") == 2
    assert candidate("You and I are going for a walk") == 0
    assert candidate("The sky is blue. The sun is shining. I love this weather") == 1


check(is_bored)