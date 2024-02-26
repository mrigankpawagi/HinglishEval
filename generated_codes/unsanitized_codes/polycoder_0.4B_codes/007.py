from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Diye gaye input list ko sirf un strings ke liye filter karo jo diye gaye substring ko contain karti hain
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    match = True
    strs = utils.simple_split(substring,'')
    pattern_num = len(strs) - 1
    new_strs = list()
    for c in strs:
        index = utils.find_start_of_word(c, pattern_num)
        if not index:
            continue
        new_str = c[index + 1:]
        if not utils.match_string(new_str, match):
            match = False
        if not match:
            new_strs.append(c)
    return new_strs

