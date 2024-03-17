from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input ek space-delimited string hai jisme 'zero' se 'nine' tak ke numerals hain.
    Valid choices 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' aur 'nine' hain.
    Return karo string ko jisme numbers smallest se largest tak sorted honge
    >>> sort_numbers('three one five')
    'one three five'
    """   number_list = list(set(numbers))  # hai ke space-delimited string karo ek space-delimited string (all numbers from set)
    sorted_number_list = sorted(number_list, reverse=True)  # hai ke string ko ek space-delimited string to arun sorted
    return''.join(sorted_number_list)

