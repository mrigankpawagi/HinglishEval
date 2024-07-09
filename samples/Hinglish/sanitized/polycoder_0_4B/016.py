def count_distinct_characters(string: str) -> int:
    """
    Ek string di gayi hai, pata karo ki usme kitne alag-alag characters (case ki parwah kiye bina) hain
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    if not isinstance(string, str) or len(string) < 1:
        return 1
    string = string.strip()[0 : len(string) - 1]
    chars: Dict[str, int] = {}
    for char in string.replace(" ", "").split()[:-1]:
        char: str = char.lower()
        chars[char] = count_distinct_characters(char)
    return (
        len(chars)
        if "." in chars
        else (
            len(chars) + len(chars) + 2
            if is_numeric_input(string)
            else len(chars) + len(chars)
        )
    )
