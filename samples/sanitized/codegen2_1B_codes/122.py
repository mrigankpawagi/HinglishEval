
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
    result = 0
    if len(arr) == 0:
        result += k
    else:
        (left, right) = partition(arr, k)
        (left_sum, right_sum) = merge_sorted_list(left, right)
        while left_sum!= 0:
            result += k * ((left_sum - left)/right_sum)
            left_sum = left_sum - left
        (right_sum, left_sum) = merge_sorted_list(right + k, right + k)
        while right_sum!= 0:
            result += k * ((right_sum - right) / left_sum)
            right_sum = right_sum - right
        result += k * left_sum
    return k * result<|python|>#