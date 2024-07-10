from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    input_number = []

    for char in numbers.split():
        if char.isnumeric():
            number = int(char)
            input_number.append(number)
        else:
            if number >= 8 and number < 10:
                number -= 1
            number = 0

    return ' '.join([str(n) for n in sorted(input_number)])
