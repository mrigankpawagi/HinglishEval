
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

    arr = sorted(arr)
    k = 10

    # print("arr = {} k = {}".format(arr,k))
    subSums = dict()
    for i, elem in enumerate(arr):
        if elem in subSums.keys():
            subSums[elem] += k
        else:
            # elem in subSums,so update its subSums value
            subSums[elem] = k
    # print('subSums = {}'.format(subSums))

    dp =  [0] + [10 ** 5 + 1 for _ in range(len(arr))]
    # print('DP[0] = {}'.format(dp))
    for j, elem in enumerate(arr):
        for i, subS in subSums.items():
            if elem > i:
                continue
            subDiff = i - elem
            subSum = subDiff + elem
            curr_max = dp[j-1] + subS + subSum
            if curr_max <= dp[j]:
                dp[j] = curr_max
            # print(f"subDiff = {subDiff}, {elem}")

    # print(dp)
    return dp[-1]

