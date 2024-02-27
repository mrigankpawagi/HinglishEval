from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input ek space-delimited string hai jisme 'zero' se 'nine' tak ke numerals hain.
    Valid choices 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' aur 'nine' hain.
    Return karo string ko jisme numbers smallest se largest tak sorted honge
    >>> sort_numbers('three one five')
    'one three five'
    """   if not (isprint(numbers) or numbers[-1] in 'f'):
        raise ValueError(
            "Number must be a number in the right format "
            "'--', 'f' or an appropriate number type is specified. Available types: "
            "'f','g','k','h'"
        )
    try:
        numbers = str(numbers)
    except ValueError:
        return numbers
    if math.isnan(numbers):
        return numbers
    if not math.isinf(numbers):
        return sorted(numbers, key=operator.itemgetter(-math.isnan))[1]
    return numbers.replace('.','/')

