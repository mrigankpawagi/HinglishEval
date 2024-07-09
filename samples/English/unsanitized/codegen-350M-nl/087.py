
def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2)...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    a = lst
    for item in a:
        if item in x[1]:
            x[1][ item] = [
                x[1][ item] if item not in x else x[item]
            ]
    return x

If both have a number of columns similar to the output above, the answer is an answer to the question in the title.
This is still a bit of a bit messy solution.  For that, you can use the dictionary comprehension approach, which has an easy "if" clause to avoid needing to have the tuples evaluated at all times.

