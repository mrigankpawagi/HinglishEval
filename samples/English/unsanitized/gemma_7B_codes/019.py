from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input ek space-delimited string hai jisme 'zero' se 'nine' tak ke numerals hain.
    Valid choices 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' aur 'nine' hain.
    Return karo string ko jisme numbers smallest se largest tak sorted honge
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.split()
    num2num = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    # print(num2num)
    for i in range(0, len(numbers)):
        s = numbers[i].split("")
        # print(s)
        numbers[i] = int(s[len(s)-1])
    # print(numbers)
    numbers.sort()
    # print(numbers)
    final = " ".join(map(str, numbers))
    # print(final)
    return final[0:len(final) - 1]


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
