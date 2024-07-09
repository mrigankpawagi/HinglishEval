
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    
    # TODO
    # Implement your function here
    
    # complete this method

if __name__ == "__main__":
    print("Example 1:")
    print("Input : ")
    print("nums = [-2, -3, -4, -2, 0, 0, 1, 2, 3, 4, 5]")
    print("Exception : ")
    print("[ -2, -5, -2, 0, -3, -2, -4 ]")
    print("Output :")
    print(sort_array([-2,-3,-4,0,-2,-3,1,1,4,-2]))
    print()
    print_divisible_by_2 = False
    print("Example 2:")
    print("Input : ")
    print("nums = [-2, -3, -4, -5, 6]")
    print("Exception : ")
    print("[-3, -4, -5, 6]")
    print("Output :")
    print(sort_array([-2,-3, -4, 5,-5, 6, 7, 5, 8]))
    print()
    print_nearly_divisible_by_3 = False
    print("Example 3:")
    print("Input : ")
    print("nums = [5, 10, 12, 6, 6]")
    print("Exception : ")
    print("[20, 12, 16, 8]")
