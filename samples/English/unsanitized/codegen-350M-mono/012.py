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
    length = 1
    index = -1

    for i, s in enumerate(strings):
        if len(s) > length:
            length = len(s)

    for i, s in enumerate(strings):
        for j, sj in enumerate(strings):
            if i < j:
                if s[i : i + int(length / 2)]!= sj[j : j + int(length / 2)]:
                    return s[i : i + int(length / 2)]

        if index >= 0 and i!= index:
            return None

    return None


