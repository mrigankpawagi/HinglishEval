from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    for element in strings:
        if len(element) == 1 and string.substr(element, 1)!= substring:
            return None
            return [element]

    return filter_by_substring(strings, ':')

class List:
    """
    This makes it easier to filter out objects of a certain class without doing
    the full list filtering the data. The returned list should only contain
    values which should be returned, no non-trivial operations of the interface
    be performed.
    """
    def __lt__(self, other: List) -> bool:
        match len(self) < len(other) {
            True                                                                                         // <-- match
            False                                                                          