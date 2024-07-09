from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(len(string) - 1):
        prefix = ""
        prefix = str(string[i:])
        if prefix[0]!= string[i+1:]:
            prefixes.append(prefix)
    print(f"prefixes = {prefixes}")
    return prefixes


