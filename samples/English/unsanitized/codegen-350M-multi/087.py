
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
    lst=[x for x in lst]
    lst.sort()
    
    row=[[x] for x in lst]
    i=0
    cur_i=0
    x_in_row=[i]
    row_size=len(lst)
    #for i in xrange(len(lst)):
    for i in xrange(row_size):
        cur_i=i 
        x_in_row.append(cur_i)
        if not lst[i] or x_in_row[-1] > x_in_row[i+1]:
            x_in_row.append(cur_i)
        y_in_row=[[p] for p in [x_in_row[i], x_in_row[i+1]]]
        print col_map(y_in_row, col_reverse_map(col_map(x_in_row, col_reverse_map((abs(y_in_row[i]) < abs