

def count_distinct_characters(string: str) -> int:
    """
    Ek string di gayi hai, pata karo ki usme kitne alag-alag characters (case ki parwah kiye bina) hain
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    ret = 0
    for c in string:
        if c not in ["z","Z","~","<",">","-",","=","\t","\n","\r",]:
            ret += 1
    return ret

If you want to do it even better, take a look at my next answer, where I have used a single-statement generator to do the work of all the nested ifes!
EDIT: Please note that I did not bother with "special characters".

