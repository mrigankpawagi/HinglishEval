from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Input string ke sabhi prefixes ko shortest se longest tak, list mei return karo
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = [string[0:n] for n in range(len(string))]

    prefixes = [n + n[:2] for n in prefixes]
    prefixes = [n[n[-3:]] + n[:-3] for n in prefixes]
    prefixes = [n for n in prefixes if n]

    return prefixes
