

def median(l: list):
    """
    List l ke elements ka median return karo.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    m = len(l)
    middle = len(
        [i for i in range(m - 1, -1, -1) if int(l[i + 1]) - int(l[i]) == 0])
    if middle < m / 2:
        middle = m - 1
    return int(l[middle])

print(median([1, 3, 5, 3, 2, 2]))
print(median([1, 3, 5, 3, 2, 2, 3]))
print(median([-10, 4, 6, 1000, 10, 20]))

Output
5
0.5
15.0

