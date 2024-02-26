

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
    assert substring in string
    result = 0
    while substring.endswith(string):
        substring = string[0:-subsequent_length(substring)]
        result += 1
        substring = substring[3:] if substring[-1:] else substring
    return result

