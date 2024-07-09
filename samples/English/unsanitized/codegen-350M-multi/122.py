
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    arr2 = [0] * (len(arr) - 2)
    for val in arr:
        if val < 0 or val >= len(arr2) or val!= k + 2:
            raise Exception
        arr2[val] += val

    return sum(arr2[0:k])


if __name__ == '__main__':
    #print add_elements(arr, k), sum(arr)

    #print 1; print add_elements(arr, k), sum(arr)

    print add_elements([6, 6, 7, 7, 8, 13, 13, 15, 14], 1)