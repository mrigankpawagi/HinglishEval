
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
    len_arr = len(arr)
    arr_elements = [[0, 0, 0, 0] for i in range(len_arr)]
    arr_length = [len_arr, 1, 1, 1]
    sum_arr = [[0, 0, 0, 0] for i in range(len_arr)]
    max_len_arr = [len_arr, 1, 1, 1]
    arr_sum_values = len_arr * [0, 0, 0, 0]
    arr_max_length = [len_arr, 1, 1, 1]
    arr_max_sum_values, max_len_arr = [0, 0, 0, 0], [len_arr, 1, 1, 1]
    arr_sum = 0
    max_sum = 0
    min_len = len_arr
    for i, element in enumerate(arr):
        sum_arr[min_len][4] = sum_arr[min_len][4] + element.count(1)
        arr_sum_values[min_len] = arr_sum_values[min_len] + (element.find(1) + 1)
        if element[0] + element[1] == 1:
            arr_