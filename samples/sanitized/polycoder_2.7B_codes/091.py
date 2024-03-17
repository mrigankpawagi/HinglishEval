
def is_bored(S):
    """
    Aapko ek string di jayegi jisme words honge, aur aapka task hai ginna ki kitne boredoms hai. Ek boredom woh sentence hota hai jo "I" word se start hota hai.
    Sentences ko '.' , '?' ya '!' se alag kiya jata hai.
   
    Udaharan ke liye:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """    import re
    s = S.lower()

    if "yes" in s or "y" in s or "ye" in s:
        return 1
    elif "no" in s or "n" in s or "ne" in s or "no" in str(S).lower():
        return 0
    else:
        return 2




