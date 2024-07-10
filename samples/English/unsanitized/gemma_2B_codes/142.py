


def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    result = 0
    for i in lst:
        if i % 3 == 0 or i%4 == 0:
            result += int(i**3)
        else:
            result += int(i)
    return result


def print_sum_square(arr):
    for i in range(0, len(arr), 1):
        print(sum_squares(arr[i]))


print_sum_square([1, 2, 3, 4, 5, 6])
print(sum_squares([1, 2, 3, 4, 5, 6]))
print(sum_squares([1, 2, 3, 4, 5, 6]))
print(sum_squares([1, 2, 3, 4, 5, 6]))
