
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    min_size = len(arr)
    # The first element can change to any other element
    change_list = []
    for i in range(min_size):
        change_list.append(i)
    change_list.sort()
    for i in range(len(arr)-1, 0, -1):
        num_change = len(arr[i+1:]) - len(arr[i+2:])
        if num_change < 0:
            continue
        for j in range(change_list[0], change_list[-1] + 1):
            new_number = j if num_change > 0 else numpy.where(arr[i:j+1] == arr[:j+1])[0]
            if num_change > 0:
                arr[i:j+1] = arr[new_number]
            else:
                arr[j+1:] = arr[new_number]

    return numpy.amin(arr[:-1]) + 1

if __name__ == '__main__':
    print smallest_change([10,12,15,11,9,18,16,13])
    print smallest_change([10,11,5,7,8,9,10,2])
    print smallest_change([10,11,5,7,8,9,10,2,1,3,5])
    print smallest_change([0,2,4,9,0,0,0,0])