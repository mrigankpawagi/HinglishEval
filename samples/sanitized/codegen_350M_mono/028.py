from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Strings ki list ko ek single string mein jodo
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    tmp_string = ""
    for string in strings[0]:
        tmp_string += string
    if strings[1] == "" or len(strings[1]) == 0:
        return tmp_string
    for string1 in strings[1]:
        tmp_string += string1
    return tmp_string