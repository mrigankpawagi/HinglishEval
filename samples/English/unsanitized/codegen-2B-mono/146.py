
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    numsLst = nums
    list1 = []
    num = len(nums)
    for i in range(num - 1, 0, -1):
        if nums[i] > 10:
            if nums[i] & 1 == 1 and nums[i - 1] == 0 and nums[i + 1] == 0:
                list1.append(nums[i])
    return len(list1)
                
    # Your code here

