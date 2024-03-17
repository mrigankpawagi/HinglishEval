

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
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count


def how_many_times_overlapping(string: str, substring: str) -> int:
    """
    Mool string mein diye gaye substring ko kitni baar mila ja sakta hai, yeh find karo. Overlapping cases ko bhi count karo.
    >>> how_many_times_overlapping('', 'a')
    0
    >>> how_many_times_overlapping('aaa', 'a')
    3
    >>> how_many_times_overlapping('aaaa', 'aa')
    3
    """
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
            if i < len(string) - len(substring):
                count += how_many_times_overlapping(string[i+len(substring):], substring)
    return count


def how_many_times_overlapping_2(string: str, substring: str) -> int:
    """
    Mool string mein diye gaye substring ko kitni baar mila ja sakta hai, yeh find karo. Overlapping cases ko bhi count karo.
    >>> how_many_times_overlapping_2('', 'a')
    0
    >>> how_many_times_overlapping_2('aaa', 'a')
    3
    >>> how_many_times_overlapping_2('aaaa', 'aa')
    3
    """
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
            if i < len(string) - len(substring):
                count += how_many_times_overlapping_2(string[i+len(substring):], substring)
    return count


def how_many_times_overlapping_3(string: str, substring: str) -> int:
    """
    Mool string mein diye gaye substring ko kitni baar mila ja sakta hai, yeh find karo. Overlapping cases ko bhi count karo.
    >>> how_many_times_overlapping