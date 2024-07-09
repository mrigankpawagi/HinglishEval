
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    
    nA = len(nums)
    
    l = len(nums[0])
    
    count1, count2 = 0, 0
    for i in xrange(nA - 1):
        
        last = nums[i][l-1]
        if int(last) == i:
            count1 += 1
        if last % 2 == 0 and int(nums[i][0]) % 2 == 1:
            count2 += 1
        elif last % 2 == 0 and last < 0:
            count2 += 1
        
        pass
    
    return count1, count2

print specialFilter( [33,-2, -3,45,21,109] )

Output:
[(1, 2)]

A:

There are many ways to do it and each way has its pros and cons and each language has its own language features.
The best way is probably something like this. If you think you need such a hack, do look for existing functionality, which handles this, i.e. you find some library which does this for you. But for small applications, like that, you probably won't be faster with a hack as yours.
>>> def a(i):
...     if i % 10 == 0 and