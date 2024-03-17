
def count_nums(arr):
    """
    Ek function likho count_nums jo ek array of integers leta hai aur return karta hai
    un elements ki sankhya jinka digits ka sum > 0 hota hai.
    Agar koi number negative hai, to uska pehla signed digit negative hoga:
    jaise ki -123 ke signed digits hote hai -1, 2, aur 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    counts = 0
    if len(arr) == 0:
        return counts
    result = 0
    nums = arr[:]
    for i in range(len(nums) - 1):
        if nums[i] < 0:
            return count_nums(nums) - nums[i]
        result += nums[i]
    return nums[0] + sum(result)