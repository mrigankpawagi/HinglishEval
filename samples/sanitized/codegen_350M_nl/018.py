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
    # split string with delimiter and count.
    # take count as 1
    count = 0
    for k in string.split(delimiter):
        # parse delimiter
        str_and_count = k + ":".join(delimiter)
        # count count
        count = count + str_and_count.count(" ")
    return count