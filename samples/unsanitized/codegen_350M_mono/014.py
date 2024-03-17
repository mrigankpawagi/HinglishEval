from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Input string ke sabhi prefixes ko shortest se longest tak, list mei return karo
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    
    s = str.split(string)
    longest = str(' '.join(s): len(max(s, key=len)))
    shortest = str(' '.join(s): len(min(s, key=len)))
    outputs = [longest, shortest]
    # outputs = [longest]
    prefixes = ['']
    for i in range(6):
        prefix = prefixes[i]
        if len(prefix) > len(string):
            prefixes.append()
            prefix = prefixes[i:i+len(string)]
    return inputs + prefixes


