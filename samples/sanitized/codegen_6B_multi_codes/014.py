from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Input string ke sabhi prefixes ko shortest se longest tak, list mei return karo
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string = "{}".format(string)
    return sorted(prefixes(string) + [lengths(string)], key=len)[::-1]