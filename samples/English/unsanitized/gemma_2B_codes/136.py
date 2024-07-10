
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
    '''
    Solution: Check if the list if negative or not, if both are negative return both
    '''
    if lst:
        if all([i < 0 for i in lst]):
            return min(lst), -max(lst)
        if all([i > 0 for i in lst]):
            return max(lst), min(lst)
    return None, None


lst = [-9000000, -25000000, -345, 345, 23456, 1]
result = largest_smallest_integers(lst)
print("result: ", result)  # result:  (None, 1)
lst = [-1, -2, -1, -2, 0, 0, -1]
# Test cases:
print(largest_smallest_integers(lst))
print(largest_smallest_integers([]))
print(largest_smallest_integers([0]))
try:
    print(largest_smallest_integers([1, 2, 3]))
except ValueError as e:
    print(e)
try:
    print(largest_smallest_integers([0, -1]))
except ValueError as e:
    print(e)
try:
    print(largest_smallest_integers([]))
except Exception as e:
    print(e)
print(largest_smallest_integers([300, -1]))
