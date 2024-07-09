
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def filterNum(x):
        return x % 10 == 1 and (x % 10 > 2 or x % 10 == 5)
    def isOdd(n):
        return filterNum(n) and filterNum(n) == filterNum(n + 1)
    return filterNum, isOdd

