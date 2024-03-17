

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
    # loop ka use kar ke liye 
    # har match hoga wo match hoga wo count kar ke baar, unko match hoga wo increment kar ke baar.

    # find(substring) method ka use karke ki value return karega!
    index = string.find(substring)
    while index!= -1:
        
        index = string.find(substring, index + 1, len(string))
        count += 1

    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    