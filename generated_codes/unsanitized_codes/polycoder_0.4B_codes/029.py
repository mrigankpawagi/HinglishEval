from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Diye gaye prefix se shuru hone wale strings ke liye input list ko filter karo.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    list_of_strings = list(set(strings) | set(filter_prefix(prefix)))
    out = []
    while list_of_strings:
        list_of_strings = set(filter_prefix(prefix + str(i) for i in list_of_strings))
        if out:
            return out + list_of_strings
        list_of_strings = set(filter_prefix(prefix + str(i) for i in list_of_strings))
