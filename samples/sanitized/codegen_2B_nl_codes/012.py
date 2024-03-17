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
    longest = None
    if not strings:
        return None
    while longest is None or len(str(longest)) < len(str(len(strings))):
        if any(s != longest for s in strings):
            longest = any(s != longest for s in strings)
        else:
            longest = len(strings)
    return longest