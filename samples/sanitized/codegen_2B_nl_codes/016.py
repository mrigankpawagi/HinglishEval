

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
