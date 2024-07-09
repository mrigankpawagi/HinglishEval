

def median(l: list):
    """
    List l ke elements ka median return karo.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """   # Sorting the list
    sortedList = sorted(l)
    # Computing the median
    if len(sortedList) % 2 == 0:
        if len(sortedList) == 1:
            return sortedList[0]
        return (
            sortedList[len(sortedList) / 2] + sortedList[(len(sortedList) / 2) - 1]
        ) / 2.0
    else:
        return sortedList[len(sortedList) / 2]

