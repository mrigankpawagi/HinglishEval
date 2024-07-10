from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """
    Diye gaye integers ki list mei se, sequence me diye gaye har moment tak paye gaye rolling maximum element ki list generate karo.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    pass


def num_even(numbers: List[int]) -> Tuple[int, int]:
    """
    Diye gaye integers ki list mei se, har index ki even position pe walay element ki number jo ki list me present ho (ei list mei koi bhi duplicate element nahi chahiye), jo ki list mei even position par present ho, un ki number jo ki is list me present ho, un ko list mei jaye ga:
    >>> num_even([17, 31, 4, 11, 26, 2, 1, 2, 3, 4])
    (17, 26, 1, 2, 3)
    >>> num_even([])
    ()
    """
    pass


def even_odd(numbers: List[int]) -> Tuple[List[int], List[int]]:
    """
    Har integer ki list mei, un sublists ko generate karo jo ki list mei alag even or odd elementon par walay sublist ko alag alag sublist ko list mei jaye ga:
    >>> numbers = [-1, 0, 99, 200, 205, 197, 112, 113, 114, 115, 1, 2]
    >>> even_odd(numbers)
    ([-1, 0, 2, 200, 205, 112, 1, 2], [99, 197, 113, 114, 115])
    """
    pass


def count_vowels(words: List[str]) -> List[int]:
    """
    Har string ki list mei walay word mei present walay vowels (aeiou) ki count karai gi or un ko list mei jaye ga
    >>> count_vowels(["apple", "orange", "banana", "papaya"])
    [5, 5, 3, 3]
    """
    pass


def count_consonants(words: List[str]) -> List[int]:
    """
    Har string ki list mei walay word mei present walay consonants (aeiou) ki count karai gi or un ko list mei