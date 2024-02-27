
def is_bored(S):
    """
    Aapko ek string di jayegi jisme words honge, aur aapka task hai ginna ki kitne boredoms hai. Ek boredom woh sentence hota hai jo "I" word se start hota hai.
    Sentences ko '.' , '?' ya '!' se alag kiya jata hai.
   
    Udaharan ke liye:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """    s = S
    ans = {'.':0, '?': 0, '!': 0, '\n': 0, '.': 0, '?': 1, '!': 1}    # 1 for true word, 0 for false words
    s = s.strip()
    if s == '':
        return 0
    i = 1      # the letter in current string
    j = 1      # the letter in current letter in S[1::2]
    h = 0      # word is HARD
    c = 0      # word is CHALL
    u = 0      # word is UNEXPECT
    nul = 0    # string is NULL
    if len(s) > 1:
        for k in [1, 2]:
            if k == len(s):
                if s[k] == s[k-1]:
                    # The second letter is same as the first.
                    if k == 1:
            