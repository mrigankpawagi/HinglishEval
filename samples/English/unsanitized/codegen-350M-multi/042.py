

def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    result = l
    while True:
        try:
             if len(result) is not 0:
                 result.append(result[0] + 1)
                 result.append(result[1])
                 result.append(result[2])
                 result.append(result[3])
             result.append(result[0])
             result = result[1:]
         except IndexError:
             break
   return result

print(incr_list(range(4, 10)))
print(incr_list(range(10, 19)))
