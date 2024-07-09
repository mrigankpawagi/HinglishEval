
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    nums = [[-1, 0x1] for _ in range(len(nums))]
    extra = set()
    for num in nums:
        if extra in num:
            num += extra
    def specialFilter_plus_1_digits(num):
        """Write a function that takes two numbers as input and returns 
        the number of elements in the array that are not greater than 
        10 (only last digits are odd) and also returns the first and only
        digit (or -digits) of the number for this return value."""
        num = np.array(num, dtype=numpy.dtype([[]], order='-1')).astype(numpy.uint8)
        numer = np.array([-np.max(num)], dtype='uint8')
        num -= [1]  # -1
        if num < len(num):
            extra = add(numer, num)
        else:
            if extra == 0:
                extra = num - 0
            num = num - extra
            numer = num
     