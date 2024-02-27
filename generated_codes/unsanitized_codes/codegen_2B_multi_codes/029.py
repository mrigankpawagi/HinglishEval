from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Diye gaye prefix se shuru hone wale strings ke liye input list ko filter karo.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    new_strings: List[str] = []
    for i, str_ in enumerate(strings):
        if str_.startswith(prefix):
            new_strings.append(str_)
    return new_strings


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert validate_no_duplicates(
        filter_by_prefix("abcd", "d")
    ), "test 'validate_no_duplicates' need check 'for case 1'"
    assert validate_no_duplicates(
        filter_by_prefix("aabcde", "def")
    ), "test 'validate_no_duplicates' need check 'for case 2'"
    assert validate_valid_pairs(
        filter_by_prefix(["abcd", "cde"], "abcd")
    ), "test 'validate_valid_pairs' need check 'fou case 1'"
    assert validate_valid_pairs(
        filter_by_prefix(["abcd", "cde"], "abbc")
    ), "test 'validate_valid_pairs' need check 'fou case 2'"
    assert not validate_valid_pairs(
        filter_by_prefix(["abcd", "cde", "array"], "abc")
    ), "test 'validate_valid_pairs' don't need check 'fou case 3'"
    assert not validate_valid_pairs(
        [1, 2, 3, 1, 2, 3], [1, 2, 2, 2, 2]
    ), "test 'validate_valid_pairs' don't need check [3, 1, 3, 4, 3]"
