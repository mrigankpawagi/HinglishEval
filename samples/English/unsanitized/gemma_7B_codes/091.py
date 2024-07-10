
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
    return len([s for s in S.split('.') if s.strip()[:1]=="I" or s.strip()[:1]=="i"])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
