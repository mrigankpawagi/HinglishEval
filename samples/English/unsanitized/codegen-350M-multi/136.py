
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
    maximal = []

    for x in lst:
        if x is None:
            x = None
        else:
            if x < 0:
                x = None
            else:
                x = x + 1

        if x > 0.0:  # Check if x > 0
            if x > maximal[-1][0]:
                maximal.append((x, maximal[-1]))
                x = None
            else:
                for y in maximal[:-1]:
                    if x > y[0]:
                        x = y[1]
                        break
    if maximal[-1][1] is not None:
        return minimal[-1][0], max(maximal[-1][0], maximal[-1][1])
    return minimal[-1][0], None
