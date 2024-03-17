from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Input string ke sabhi prefixes ko shortest se longest tak, list mei return karo
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(len(string) + 1)]


def all_suffixes(string: str) -> List[str]:
    """
    Input string ke sabhi suffixes ko shortest se longest tak, list mei return karo
    >>> all_suffixes('abc')
    ['c', 'bc', 'abc']
    """
    return [string[i:] for i in range(len(string) + 1)]


def all_anagrams(string: str) -> List[str]:
    """
    Input string ke sabhi anagrams ko shortest se longest tak, list mei return karo
    >>> all_anagrams('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    """
    return [''.join(sorted(string)) for string in all_prefixes(string)]


def all_anagrams_of_length(string: str, length: int) -> List[str]:
    """
    Input string ke sabhi anagrams ko shortest se longest tak, list mei return karo
    >>> all_anagrams_of_length('abc', 2)
    ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']
    """
    return [''.join(sorted(string)) for string in all_prefixes(string) if len(string) == length]


def all_anagrams_of_length_and_prefix(string: str, length: int, prefix: str) -> List[str]:
    """
    Input string ke sabhi anagrams ko shortest se longest tak, list mei return karo
    >>> all_anagrams_of_length_and_prefix('abc', 2, 'a')
    ['ab', 'ba']
    """
    return [''.join(sorted(string)) for string in all_anagrams_of_length(string, length) if string.startswith(prefix)]


def all_anagrams_of_length_and_suffix(string: str, length: int, suffix: str) -> List[str]:
    """
    Input string ke sabhi anagrams ko shortest se longest tak, list mei return karo
    >>> all_anagrams_of_length_and_suffix('abc', 2, 'b')
    ['