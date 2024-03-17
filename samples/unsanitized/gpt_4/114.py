Sure, here is the completed Python function:

```python
def minSubArraySum(nums):
    """
    Ek integer array nums diya gaya hai, usme se kisi bhi non-empty sub-array ka minimum sum dhundho.
    Udaharan
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = min(current_sum + num, num)
        min_sum = min(min_sum, current_sum)
        
    return min_sum
```

This function uses the Kadane's algorithm to find the minimum sum of any subarray in the given list of numbers. It initializes the `min_sum` and `current_sum` to the first element of the list. Then, for each number in the list, it updates the `current_sum` to be the minimum of the current sum plus the number and the number itself. It also updates the `min_sum` to be the minimum of the `min_sum` and the `current_sum`. Finally, it returns the `min_sum`.