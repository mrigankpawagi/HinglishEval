
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
    # this is the output string
    s = S.split('.', 1)
    s2 = s[0].split('?')
    s3 = s[0].split('!')

    # first, check for empty strings
    if len(s) == 1:
        return 0

    # check if the string ends with 'I'
    if s[1][-1] == 'I':
        return len(s2) + len(s3)

    # check if the string ends with a '.'
    if s[1][-1] == '.':
        return 1
    if s[1][-1] == '?':
        return len(s2) + 1
    if s[1][-1] == '!':
        return len(s3) + 1
                      
