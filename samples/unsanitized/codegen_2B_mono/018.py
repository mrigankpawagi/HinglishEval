

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
    for i in range(len(string)-len(substring)+1):
        if string[i:i+len(substring)] == substring:
            count = count+1
    return count



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)