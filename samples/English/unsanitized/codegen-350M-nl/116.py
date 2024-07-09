
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    counter = 1
    for i in arr:
        counter += i
    return counter  

The above answer uses 'count' column in each row, and then sort in ascending order by 'count' column, it is possible, but would be much better to use 'bin' column, because that would make sort() in Python 2, and to use 'decimal' as number of number elements, it's possible to calculate number in single step.
So you have to find out how many of your number elements need to be inserted in the correct order in binary order.
For example, in binary order:
>>> bin = [n for n in sorted(len(a)) if n % 2 == 1]

You can find out how many of the number you have to insert in the correct order.
Finally, you can use this code to create a list from your array of integers in descending order:
