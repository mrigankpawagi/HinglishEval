
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
    def add_digits(n):
        arr = list(str(n))
        if len(arr) == 1:
            return int(arr[0])
        for i in range(len(arr)-1):
            arr[i] = int(arr[i])+int(arr[i+1])
            if arr[i] > 9:
                arr[i] = int(arr[i])%10 + int(arr[i-1])
                arr[i-1] = arr[i]
        return arr

    ans = 0
    for n in arr:
        ans += add_digits(n % 1000000000)[0]
    return ans % (10**k)
