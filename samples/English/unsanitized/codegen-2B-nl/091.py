
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
    bored_count = 0
    for sentence in S:
        if sentence == "I":
            bored_count += 1        
    return bored_count

There are a few details I've left out of the code, but the pattern really is obvious once you figure how to create a function (or generator function) that only outputs the results you want.
That said, a generator function like this is not suitable for use with a for loop.
The for... in syntax was designed originally for looping over a bunch of iterables (lists), in order to get the index of the last one processed, and it's still used like that in Python.
However, a good iterator, or dataflow programming style, uses one or more iterators over each item in the sequence, along with a one-shot sequence producer. This is a sequence that yields the entire sequence of results a single time:
