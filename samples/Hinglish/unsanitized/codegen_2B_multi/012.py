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
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return set(strings)[0]
    if len(strings) < 3:
        return strings[0]
    return longest([s.upper() for s in strings] + [s.lower() for s in strings])
