def count_distinct_characters(string: str) -> int:
    """
    Ek string di gayi hai, pata karo ki usme kitne alag-alag characters (case ki parwah kiye bina) hain
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    count = {}
    for character in string:
        character_key = character.upper()
        if character not in count:
            count[character_key] = 1
        else:
            count[character_key] += 1
    return len(count) - 1