
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    seen = {}
    def unique_digits(nums):
        n = len(nums) - 1
    
        for i in range(len(nums) - 1):
            key = nums[i]
            if key in seen:
                continue
            seen[key] = True
            nums[i], nums[n] = nums[n], nums[i]
            if nums[i] % 10 == (nums[n] + 1) % 10:
                nums[i], nums[n] = (nums[i] + 1) % 10, nums[n]
            if nums[n] % 10 == (nums[i] + 1) % 10:
                nums[n], nums[i] = (nums[i] + 1) % 10, nums[n]

    # Call on every value in nums.
    unique_digits(x)
    
    seen = list(seen.keys())
    unique_nums = []
    for key in seen:
        s = sum(nums)
        if key == s:
            break
        else:
            unique_nums.append(key)
    
    if len(unique_nums) == 0:
        return []
    
    return unique_nums

