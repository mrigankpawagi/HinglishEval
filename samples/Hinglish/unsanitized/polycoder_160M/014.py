from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Input string ke sabhi prefixes ko shortest se longest tak, list mei return karo
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    out = []
    for i in range(len(string)):
        if i in string:
            out.append(string[:i])
            out.append(string[(i + 1) : (i + 1)] + string[i:])
    return out
