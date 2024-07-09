from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Diye gaye prefix se shuru hone wale strings ke liye input list ko filter karo.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """
    Diye gaye suffix se shuru hone wale strings ke liye input list ko filter karo.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['bcd', 'cde']
    """
    return [s for s in strings if s.endswith(suffix)]


def filter_by_length(strings: List[str], length: int) -> List[str]:
    """
    Diye gaye length se shuru hone wale strings ke liye input list ko filter karo.
    >>> filter_by_length([], 3)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 3)
    ['abc']
    """
    return [s for s in strings if len(s) == length]


def filter_by_length_and_prefix(strings: List[str], length: int, prefix: str) -> List[str]:
    """
    Diye gaye length and prefix se shuru hone wale strings ke liye input list ko filter karo.
    >>> filter_by_length_and_prefix([], 3, 'a')
    []
    >>> filter_by_length_and_prefix(['abc', 'bcd', 'cde', 'array'], 3, 'a')
    ['abc']
    """
    return [s for s in strings if len(s) == length and s.startswith(prefix)]


def filter_by_length_and_suffix(strings: List[str], length: int, suffix: str) -> List[str]:
    """
    Diye gaye length and suffix se shuru hone wale strings ke liye input list ko filter karo.
    >>> filter_by_length_and_suffix([], 3, 'a')
    []
    >>> filter_by_length_and_suffix(['abc', 'bcd', 'cde', 'array'], 3, 'a')
    ['bcd']
    """
    return [s for s in strings