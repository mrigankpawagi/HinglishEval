from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Input string ke sabhi prefixes ko shortest se longest tak, list mei return karo
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    res = []
    longest = 0
    for i in range(len(string)):
        prefix = string[i]
        if (prefix >= longest):
            longest = prefix
        elif (prefix < longest):
            res.append(prefix)

    return res


