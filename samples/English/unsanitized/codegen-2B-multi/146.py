
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    numFound = 0
    for i in range(0, len(nums)):
        if i == len(nums) - 1: break
        
        # If the current element is greater than 10, or both the first and 
        # the last
        # digits of the current element are both the odd numbers, break.
        if nums[i] >= 10:
            if (nums[i] % 10 % 5==1 | nums[i] % 10 % 1==1):
                numFound += 1
                break
    return numFound
