

def count_distinct_characters(string: str) -> int:
    """
    Ek string di gayi hai, pata karo ki usme kitne alag-alag characters (case ki parwah kiye bina) hain
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    
    count = 0
    for c in string:
        count = count + 1
    return count


