

def how_many_times(string: str, substring: str) -> int:
    """
    Mool string mein diye gaye substring ko kitni baar mila ja sakta hai, yeh find karo. Overlapping cases ko bhi count karo.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # Get the indices of the end of the substring in this string
    indices_end = string.find(substring, pos="last")
    if indices_end is not None:
        # Get the index of a substring in the full string which is right after this substring.
        right_idx = string.find('', pos=indices_end + len(substring))
        # Get substring indices which contains substring in between two indices.
        indices_in_between = string[right_idx:]
        # Find these indices and count the number of index that contains a substring.
        count = len(set(indices_in_between) - set(string.find(substring, pos=0))))
    else:
        count = -1
    return count
