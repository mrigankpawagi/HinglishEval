def count_distinct_characters(string: str) -> int:
    """
    Ek string di gayi hai, pata karo ki usme kitne alag-alag characters (case ki parwah kiye bina) hain
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string = sorted(string.lower())
    print(string)
    count = 0
    for char in string:
        if char in string[:-1]:
            print(f"{count} {string.count(char)}")
            count += 1
        else:
            count = 0