from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if len(strings) == 0:
        return None

    ret = strings[0]
    for s in strings[1:]:
        if len(s) > len(ret):
            ret = s

    return ret


if __name__ == '__main__':
    from doctest import testmod
    testmod()
