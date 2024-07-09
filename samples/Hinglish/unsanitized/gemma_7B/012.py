from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    String ki list se, sabse lamba string return karo. Agar same length ke multiple strings ho to pehla string return karo. Agar input list khali ho to None return karo.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if len(strings) == 0:
        return None
    max_len = 0
    max_str = ""
    for string in strings:
        if len(string) > max_len:
            max_len = len(string)
            max_str = string
    return max_str


if __name__ == "__main__":
    import doctest

    doctest.testmod()
