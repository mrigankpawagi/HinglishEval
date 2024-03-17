def median(l: list):
    """
    List l ke elements ka median return karo.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sorting the list
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


print(median([3, 1, 2, 4, 5]))

t1 = (median([3, 1, 2, 4, 5]) + median([2, 5, 4, 3, 1])) / 2.0
print("median - Sorted list: ", t1)

# print(min(2,3,4,5))
# print(max(2,3,4,5))

# def main():
#    print('TEST 1')
#    l = [3,1,2,4,5]
#    #print(min(l)) print('Median - Sorted list: ', t1)
#    #return min(l)
#    #print("The min element: %d" % min(l))
# print(max(l)) print('Median - Sorted list: ', t1)
