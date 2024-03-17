

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

    if not substring:
        return 0

    if string.startswith(substring):
        return 1

    if len(string) == len(substring):
        return string.count(substring)

    return 0

if __name__ == '__main__':
    how_many_times('bcc', 'abc')

