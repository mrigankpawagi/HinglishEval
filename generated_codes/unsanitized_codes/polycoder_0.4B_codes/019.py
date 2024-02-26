from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input ek space-delimited string hai jisme 'zero' se 'nine' tak ke numerals hain.
    Valid choices 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' aur 'nine' hain.
    Return karo string ko jisme numbers smallest se largest tak sorted honge
    >>> sort_numbers('three one five')
    'one three five'
    """   from. import is_number, Number

    numbers = is_number(numbers)
    for k in range(1, 13):
        numbers = numbers.replace('numerals', 'nums').replace('e', 'e')

    if is_number(numbers):
        numbers = numbers.replace('numerals', 'nums')

    try:
        result = numbers[:2]
    except ValueError:
        pass
    except TypeError:
        pass

    sort_keys = ['nums', 'e', 'f', 'o', 'n']
    for sort_key in sort_keys:
        result = sort_key.join([str(i) for i in sorted(result)])
    return result

