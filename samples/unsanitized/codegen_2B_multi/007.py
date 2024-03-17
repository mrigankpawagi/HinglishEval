from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Diye gaye input list ko sirf un strings ke liye filter karo jo diye gaye substring ko contain karti hain
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """

    filtered_list: List[str] = []
    for index, string in enumerate(strings):
        substr = string.find(substring)
        if substr != -1:
            filtered_list.append(strings[index])

    # filtered_list = [i for i in strings if substring in i]
    return filtered_list
