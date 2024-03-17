from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Diye gaye prefix se shuru hone wale strings ke liye input list ko filter karo.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
<|python|>import logging

from fastapi_utils.pagination import page_response  #