

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
    count = 0
    for substring_index, substring_str in enumerate(substring.split(',')):
        if substring_str == 'a':
            count += 1
        else:
            count += int("".join((substring, substring_index, substring_str)))
    return count

