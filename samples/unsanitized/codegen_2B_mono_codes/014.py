from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Input string ke sabhi prefixes ko shortest se longest tak, list mei return karo
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    res = []
    for i in range(len(string)+1):
        for j in range(i,0,-1):
            res.append(string[:j])
    return res


