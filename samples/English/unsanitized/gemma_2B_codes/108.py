
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    numbers_greater_than = []
    for i in arr:
        if i > 0:
            numbers_greater_than.append(i)
    new_arr = numbers_greater_than

    # Iterate through the list of numbers with a sum greater than 0.
    count_greater = len(new_arr)


def main(numbers):
    """
    Write a function main which takes an input array (or list) of positive or
    negative integers.

    >>> main([1, 30, -12, 100, 45, 12])
    5
    >>> main([28, 9, 25, -45, -1])
    1
    """
    if numbers[0] > 0:
        print("There are {} numbers with a sum greater than 0.".format(len(numbers)))
        for i in numbers:
            if len(numbers[0][0]) > 0:
                numbers = [i]
    else :
        print("No numbers with a sum greater than 0")

if __name__ == "__main__":
    import doctest
    results = doctest.testmod()
    if not results.failed:
        print "All test passed. You get all the stars!"
    else:
        print "There were errors in the tests"
