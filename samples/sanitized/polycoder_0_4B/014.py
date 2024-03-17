from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Input string ke sabhi prefixes ko shortest se longest tak, list mei return karo
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string = string.lower()
    string = string.replace("-", "")
    return [i.strip() for i in string.strip().split("-", 1)]
