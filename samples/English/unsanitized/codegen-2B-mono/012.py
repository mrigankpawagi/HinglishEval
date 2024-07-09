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

    elif len(strings) == 1:
        return strings[0]

    elif len(strings) == 2:
        if strings[0] == strings[1]:
            return strings[0]
        else:
            return strings[1]

    elif len(strings) == 3:
        if strings[0] == strings[1] and strings[1] == strings[2]:
            return strings[0]
        elif strings[0] == strings[1] or strings[1] == strings[2]:
            return strings[1]
        elif strings[0] == strings[2] or strings[2] == strings[1]:
            return strings[0]
        else:
            return strings[2]
    elif len(strings) == 4:
        if strings[0] == strings[1] and strings[1] == strings[2] and strings[2] == strings[3]:
            return strings[0]
        elif (
            strings[0] == strings[1] and strings[1] == strings[2] or strings[1] == strings[2] and strings[2] == strings[3]
        ):
            return strings[1]
        elif (
            strings[0] == strings[1] or strings[1] == strings[2] or strings[1] == strings[2]
            or strings[2] == strings[3]
        ):
            return strings[0]
        else:
            return strings[3]
    elif len(strings) == 5:
        if strings[0] == strings[1] and strings[1] == strings[2] and strings[2] == strings