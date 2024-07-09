
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    x = [i for i in x if i % 2 == 0]
    x2 = sorted(list(set(x)))
    x2 = [i for i in x2 if i!= 0]
    return x2

if __name__ == '__main__':
    list1 = [1, 3, 4, 1422, 5]
    print(unique_digits(list1))
    print('-' * 50)
