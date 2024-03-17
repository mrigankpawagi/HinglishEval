from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Strings ki list ko ek single string mein jodo
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    if not strings:
        return ""
    l = ""
    for i, item in enumerate(strings, 1):
        l += item + ""
    return l