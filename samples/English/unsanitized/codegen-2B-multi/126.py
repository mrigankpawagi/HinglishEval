
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    '''
    Initialize
    '''
    temp_list = lst

    '''
    Check to see if there is only one instance of each value
    '''
    while temp_list:
        is_sorted_temp = True
        index = 1
        # Find the first element which is not unique
        for value in temp_list:
            if index!= 1 and value == temp_list[index-1]:
                return False

            else:
                index += 1

        # Remove the element, so we have only the next element.
        # and get rid of the element itself
        temp_list.pop(0)

    return True
