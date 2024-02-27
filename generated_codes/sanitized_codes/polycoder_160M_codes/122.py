
def add_elements(arr, k):
    """
    Ek non-empty array of integers arr aur ek integer k diya gaya hai, pehle k elements mein se jinme maximum do digits hai unka sum return karo.

    Udaharan:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    if arr.shape[1]!= k:
        raise RuntimeError('wrong element shape')
    arr[:, 0] *= -1
    arr[:, 1] += arr[:, 0]

    if arr.max()!= arr[0]:
        raise RuntimeError('wrong element')

    arr_to_sum = arr[0:0, :arr.shape[0]]

    # sum a uran:
    if arr_to_sum >= arr.shape[1] * k:
        # if arr is of shape (0,k)
        if arr_to_sum >= arr.shape[1] * (k - arr_to_sum):
            # all elements
            ret = arr_to_sum / arr.shape[1]
            if arr[0:0] + ret == arr.max():  # all elements
                return k + ret
            else:                          # all elements
                arr =