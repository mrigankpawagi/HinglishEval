
def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1, 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """
    arr = [x for x in arr if x % 9!= 0]
    if len(arr):
        start_of_current_digit = min([x % 9 for x in arr if x!= 0])
        midpoint_of_current_digit = start_of_current_digit + 1
        reverse_arr = [midpoint_of_current_digit for x in arr]
        reverse_arr.reverse()
        result = []
        current_digit = 0
        for i in reversed(range(start_of_current_digit, 0, -1)):
            result.append(reverse_arr[i]*10)
            new_current_digit = current_digit - i
            if abs(new_current_digit) > start_of_current_digit:
                current_digit = new_current_digit
        return result
    else:
        return []

#-----------------------------------------------------------------------------
