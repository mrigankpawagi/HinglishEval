from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Diye gaye input list ko sirf un strings ke liye filter karo jo diye gaye substring ko contain karti hain
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """

    result = []
    for word in strings:
        if word.lower().startswith(substring):
            result.append(word)
    return result


