from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string = str(string)
    return [s.startswith('a') and s[1:] for s in string.split('a') if s.startswith('a')] + \
           [s.startswith('b') and s[1:] for s in string.split('b') if s.startswith('b')] + \
           [s.startswith('c') and s[1:] for s in string.split('c') if s.startswith('c')]


