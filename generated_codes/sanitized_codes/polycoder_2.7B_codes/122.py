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
    if 1 > len(arr):
        return 0
    num = 0
    arr = re.sub("[(),]", "", arr)
    arr = map(str, arr)
    num = max(map(int, arr)) + 1
    num = max(num, k)
    return num
