from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    string_list = re.split('[ \t]+', numbers)
    # print('{}'.format(string_list))  # just to make sure everything is working
    sorted_string = sorted(string_list, key = str.casefold)
    # print('{}'.format(sorted_string))  # just to make sure everything is working
    return''.join(sorted_string)


if __name__ == '__main__':
    # get_string()
    get_strings()
    sorted_list = sort_numbers('two five four zero')  # the 'two' must precede 'five', so we need some extra processing
    print(sorted_list)
    # print('sort_numbers is working {}'.format(sort_numbers('two six four three five three')))

