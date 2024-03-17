from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input ek space-delimited string hai jisme 'zero' se 'nine' tak ke numerals hain.
    Valid choices 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' aur 'nine' hain.
    Return karo string ko jisme numbers smallest se largest tak sorted honge
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.strip().split()
    numbers_dict = {}
    for num in numbers:
        if num not in numbers_dict.keys():
            numbers_dict[num] = "0"
    numbers_sorted = []
    print(numbers_dict)
    for num in sorted(numbers_dict, key=numbers_dict.get):
        numbers_sorted.append(num)
    print(numbers_sorted)
    result = "".join(numbers_sorted)
    print(result)
    return result