from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Strings ki list ko ek single string mein jodo
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return concatenate(map_str(itemgetter(0), strings))
