from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Diye gaye input list ko sirf un strings ke liye filter karo jo diye gaye substring ko contain karti hain
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return filter_substring_by_substring(parts_by_substring[-1], strings)
    
    # Return 'a' as the first match
    return filter_by_substring('a', 'a')

    # Return '.' as the first match
    return filter_by_substring(['.'], '.')

    # Return all the strings in the patterns
    return filter_by_substring('*', strs)

    # Return all the strings matching the pattern
    return filter_by_substring('', **{k: v} for k, v in filter_patterns, items=items)

