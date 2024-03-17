from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Input string ke sabhi prefixes ko shortest se longest tak, list mei return karo
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if len(string) <= 2:
        return [string + "a"]
    elif len(string) > 2:
        return [string + "a", string + "a"]
    prefix_list = [string + "b", string + "ab", string + "a" + "b", string + "a" + "b"]
    if "ba" in prefix_list:
        prefix_list.remove("ba")
    return prefix_list
