
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    
    # make a function that keeps the numbers that have 2 dashes 
    # and have last digits odd
    def make(s):
    # make it a list that will be used to make a copy of the list
        new_list = list(s)
    # loop through the elements of the list and store them
        for i in new_list:
        # if the element has a digit, change it to be a minus, 
        # so it will be one digit, then add it to the copy
            if i.isdigit():
                new_list.remove(i)
                new_list.insert(0,'-')
        # return the new copy
        return new_list
    
    # loop through the numbers and make sure the two last digits of the current number have the smallest value
    smallest_number = make(str(min(nums)))
    smallest_number.sort()
    # loop through nums and make sure the number that it has a digit 
    # in the smallest number has the smallest value
    for i in smallest_number:
        if i.isdigit():
            if float(i) >= int(i):
                return 2
    return 3

print(specialFilter([15, -73, 14, -15]))