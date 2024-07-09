
def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    result = None

    for value in lst:
            if value < 0:
                for current_value in lst:
                    if current_value <= value:
                        result = (value, current_value)
                        break
            elif result is None:
                result = (value, value)
    return result


# TODO: Implement the function.
# For each element x in lst, return the largest number,
# and then the smallest number.
