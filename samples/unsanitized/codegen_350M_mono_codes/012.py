from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """
    String ki list se, sabse lamba string return karo. Agar same length ke multiple strings ho to pehla string return karo. Agar input list khali ho to None return karo.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    nestedList = []  # tuple of (tuple of str,string)
    for i in range(0, len(strings)):
        for j in range(i + 1, len(strings)):
            length = len(strings[i]) + len(strings[j])
            if length > max(len(strings[i]), len(strings[j])):
                nestedList += (tuple(sorted([strings[i], strings[j]])),)
    return max(nestedList, key=len)


