from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Diye gaye prefix se shuru hone wale strings ke liye input list ko filter karo.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """

    # This is a naive implementation. Let's hope for the best!
    if not strings:
        return strings

    if prefix == '':
        return strings

    if prefix not in strings:
        return []

    return [str[:len(prefix)]] + filter_by_prefix(strings, prefix)


