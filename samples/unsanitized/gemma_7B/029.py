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


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """
    Diye gaye suffix se khatam hone wale strings ke liye input list ko filter karo.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'y')
    ['array']
    """
    return [string for string in strings if string.endswith(suffix)]


def filter_by_length(strings: List[str], length: int) -> List[str]:
    """
    Diye gaye length ke saath strings ke liye input list ko filter karo.
    >>> filter_by_length([], 3)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 3)
    ['abc', 'bcd']
    """
    return [string for string in strings if len(string) == length]


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Diye gaye substring ke liye input list ko filter karo.
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if substring in string]


def filter_by_substring_length(strings: List[str], substring_length: int) -> List[str]:
    """
    Diye gaye substring length ke liye input list ko filter karo.
    >>> filter_by_substring_length([], 3)
    []
    >>> filter_by_substring_length(['abc', 'bcd', 'cde', 'array'], 3)
    ['abc', 'bcd', 'cde']
    """
    return [string for string in strings if len(string) == substring_length]


def filter_by_substring_prefix(strings: List[str], substring: str) -> List[str]:
    """
    Diye gaye substring ke liye input list ko filter karo.
