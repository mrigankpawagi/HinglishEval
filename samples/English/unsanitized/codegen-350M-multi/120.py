
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    k = int(k)
    # 满足 k 的异常就返回
    nums = [-1]*len(arr)
    k = k % len(arr)

    if k >= 0:
        for val in arr:
            if val <= k:
                nums[val] += 1
            else:
                break

    if k == 0:
        return sorted(nums)

    elif k == 1:
        h = arr[0]
        max = nums[0]
        for val in nums[:]:
            if val >= max:
                max = val
            else:
                h = val
        return [-h]

    else:
        val = arr[k - 1]
        if val >= k:
            c = val
            h = val
        else:
            c = k

        # 标准
        for i in range(c, 0, -1):
            for j in range(0, len(nums) - 1):
                if nums[j] > nums[i]:
                    h = j
                    break

        return [h, val]
