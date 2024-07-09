
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
    # Solution 1: linear traversal, O(nk) time
    def two_digit_arr(arr, k):
        if k == 0:
            ans = []
            for i in xrange(len(arr)):
                ans.append(arr[i])
            return ans
        ans = []
        for i in xrange(0, k):
            ans.append(sum(arr[:i]))
        ans[k-1] += arr[k-1]
        for i in xrange(k, len(arr)):
            ans.append(sum(arr[k:i+1]))
        return ans
        
    # Solution 2: dynamic programming, O(kn) time
    def two_digit_dp(arr, k):
        ans = 0
        dp = []
        for i in xrange(0, arr.__len__()):
            dp = sum(dp + arr[min(i+1, k):max(i+1, k)]) % 10
            ans += dp
        return ans

    if len(arr) == 0:
        return 0
    elif k == len(arr):
        return two_digit_dp(arr, k)
    elif k > len(arr):
        return 0
    else:
        return two_digit_arr(arr, k)


# Your add_elements function will be called like this:
# params = []
# for i in xrange(1, 101):
#     params.append(add_elements(arr[i], k=4))

