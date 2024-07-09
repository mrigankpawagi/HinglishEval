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
    for s in strings:
        if len(s) > len(strings[0]):
            return longest(s)
    return None