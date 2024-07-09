
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
    a, b = None, None
    for x in lst:
        if b is None or b < x < a:
            (a, b) = (x, b)
        elif x < 0:
            b = x
        else:
            a = x

lst = [5, 6, 2, 6, 2, 3]
print(largest_smallest_integers(lst))

A:

Python solution (just checking for your question):
