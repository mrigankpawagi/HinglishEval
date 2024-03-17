from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Input string ke sabhi prefixes ko shortest se longest tak, list mei return karo
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[:i+1])
    return prefixes


def all_prefixes_2(string: str) -> List[str]:
    """
    Input string ke sabhi prefixes ko shortest se longest tak, list mei return karo
    >>> all_prefixes_2('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[i:])
    return prefixes


def all_prefixes_3(string: str) -> List[str]:
    """
    Input string ke sabhi prefixes ko shortest se longest tak, list mei return karo
    >>> all_prefixes_3('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[:i+1])
    return prefixes


def all_prefixes_4(string: str) -> List[str]:
    """
    Input string ke sabhi prefixes ko shortest se longest tak, list mei return karo
    >>> all_prefixes_4('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[i:])
    return prefixes


def all_prefixes_5(string: str) -> List[str]:
    """
    Input string ke sabhi prefixes ko shortest se longest tak, list mei return karo
    >>> all_prefixes_5('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[i:])
    return prefixes


def all_prefixes_6(string: str) -> List[str]:
    """
    Input string ke sabhi prefixes ko shortest se longest tak, list mei return karo
    >>> all_prefixes_6('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[i:])
    return prefixes


def all_prefixes_7(string: str) ->