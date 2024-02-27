from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input ek space-delimited string hai jisme 'zero' se 'nine' tak ke numerals hain.
    Valid choices 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' aur 'nine' hain.
    Return karo string ko jisme numbers smallest se largest tak sorted honge
    >>> sort_numbers('three one five')
    'one three five'
    """
    from itertools import groupby
    zero, one, two, three, four, five, six, seven, eight, nine = (
        int(choice) for choice in numbers.replace(" ", "").split("")
    )
    return " ".join(
        str(val) * count
        for val, count in sorted(
            [
                (zero, 2),
                (one, 1),
                (two, 1),
                (three, 1),
                (four, 1),
                (five, 1),
                (six, 1),
                (seven, 1),
                (eight, 1),
                (nine, 1),
            ],
            key=lambda x: x[1],
        )
    )
    # return " ".join("" if count == 1 else str(val) * count for val, count in sorted(list(groupby(numbers.replace(" ", "")))))