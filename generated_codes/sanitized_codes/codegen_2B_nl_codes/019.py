from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input ek space-delimited string hai jisme 'zero' se 'nine' tak ke numerals hain.
    Valid choices 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' aur 'nine' hain.
    Return karo string ko jisme numbers smallest se largest tak sorted honge
    >>> sort_numbers('three one five')
    'one three five'
    """
    n_1, n_2, n_3 = [int(x) for x in numbers.split()]
    return (n_1 if n_1 % 3 == 0 else n_1) + (n_2 if n_2 % 3 == 0 else n_2) + (n_3 + 1)