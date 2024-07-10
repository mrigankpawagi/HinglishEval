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
    pass

def filter_greater_than(nums: List[int], threshold) -> List[int]:
    """
    [1,2,3,4,5,6,7,8,9]
    threshold=5
    ans:[6,7,8,9]
    """
    pass

def min_max(nums: List[int]) -> List[int]:
    """
    [1,2,3,4,5,6,7,8,9]
    ans:[1,9]
    :return:
    """
    pass

def remove_even(nums: List[int]) -> None:
    """
    :param nums: list of numbers.
    :return: should remove all even numbers from the nums list. Don't change variable nums.
    """
    pass


if __name__ == "__main__":
    import os
    import sys
    cwd = os.getcwd()
    sys.path.insert(0, cwd + '/..')
    from python_challenges.python_challenges.python_tests import test_runner

    def test_longest(expected: str, actual: str) -> bool:
        return expected == actual

    def test_longest_emptylist() -> int:
        assert longest([]) is None

    def test_min_max() -> int:
        assert min_max([5,4,3]) == [3,5]

    def test_min_max_two_numbers() -> int:
        assert min_max([1,2]) == [1,2]
    
    def test_min_max_three_numbers() -> int:
        nums1 = [1,2,3]
        assert min_max(nums1) == [1,3]
        assert nums1 == [1,2,3]
    
    def test_min_max_duplicates() -> int:
        assert min_max([2,2,3]) == [2,3]
    
    test_list = [
        test_longest_emptylist,
        test_longest
    ]
