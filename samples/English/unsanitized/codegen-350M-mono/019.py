from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    return numbers.replace('zero', '-', 1).replace('one', '-', 1).replace('two', '-', 1).replace('three', '-', 1).replace('four', '-', 1).replace('five', '-', 1).replace('six', '-', 1).replace('seven', '-', 1).replace('eight', '-', 1),


