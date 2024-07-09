from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_in_ordinal = numbers.replace('.', '0').lower()
    all_numbers_in_ordinal = [number for number in numbers]
    sort_list = []
    for number in all_numbers_in_ordinal:
        sort_list.append(number_with_length(number))
    for number in reversed(sort_list):
        del number[2:]
    for number in range(len(sort_list)):
        index = num_with_length(sort_list[number])
        if index!= 'zero':
            sort_list[index] = 'nine'
    for number in reversed(sort_list):
        index2 = num_with_length(sort_list[number])
        if index2!= 'zero':
            sort_list[index2] ='seven'
        if index2!= 'zero':
            sort_list[index2] = 'five'
        if index2!= 'zero':
            sort_list[index2] = 'one'
        if index2!= 'zero':
            sort_list[index2] = 'zero'
    return ''.join([number_with_length(number) for number in numbers])


