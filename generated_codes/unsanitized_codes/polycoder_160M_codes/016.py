

def count_distinct_characters(string: str) -> int:
    """
    Ek string di gayi hai, pata karo ki usme kitne alag-alag characters (case ki parwah kiye bina) hain
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    chars = string.encode('utf-8')
    num_chars = len(chars)
    s = string.decode('utf-8')
    return num_chars - s <= 0

