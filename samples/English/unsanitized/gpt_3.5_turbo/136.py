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
    negative_integers = [x for x in lst if x < 0]
    positive_integers = [x for x in lst if x > 0]
    
    if negative_integers:
        largest_negative = max(negative_integers)
    else:
        largest_negative = None
    
    if positive_integers:
        smallest_positive = min(positive_integers)
    else:
        smallest_positive = None
    
    return (largest_negative, smallest_positive)