from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Diye gaye input list ko sirf un strings ke liye filter karo jo diye gaye substring ko contain karti hain
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    filtered = []
    for i in strings:
        if substring in i:
            filtered.append(i)
    return filtered


# test
# >>> filter_by_substring(['abc'),''
# >>> filter_by_substring(['a', 'bc', 'cde', 'array'], 'a')
# ['bc', 'cde']

# test
# >>> filter_by_substring(['a', 'bacd', 'array'], 'b')
# []

# test
# >>> filter_by_substring(['a', 'bacd', 'cde', 'array'], 'b')
# ['a', 'array']

