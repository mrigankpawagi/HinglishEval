from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Diye gaye prefix se shuru hone wale strings ke liye input list ko filter karo.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    filtered_strings = []
    for index, prefix in enumerate(strings):
        if prefix.lower()!= prefix.upper():
            filtered_strings.append(strings[index][len(prefix):])
    return filtered_strings

