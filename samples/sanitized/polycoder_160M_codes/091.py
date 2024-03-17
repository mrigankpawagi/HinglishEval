
def is_bored(S):
    """
    Aapko ek string di jayegi jisme words honge, aur aapka task hai ginna ki kitne boredoms hai. Ek boredom woh sentence hota hai jo "I" word se start hota hai.
    Sentences ko '.' , '?' ya '!' se alag kiya jata hai.
   
    Udaharan ke liye:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """    try:
        result = re.search(r'(?i)s[/bog/g][^bog|] [a-z]{3,}|. +' + r'\1|\t', S)
    except AttributeError:
        return False, {r"s": S}
    if result is not None:
        # the first item in the sentence is broke by looking into the next sentence
        return dict(results=result, s=["bog","g","a"], bog="g", a="g")
    return False, {r"\1": ""}
