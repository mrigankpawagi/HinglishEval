
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
    if not arr:
        return arr
    if not isinstance(arr, list):
        return arr

    arr = sorted(arr)
    x = len(arr)
    y = len(arr[0])

    for i in range(x):
        arr[i] = arr[i][:y-i]

        for j in range(len(arr)):
            if arr[j] == 0:
                arr[j] = '_'


        for k in range(len(arr)):

            arr[k] = arr[k][::-1]
    
        for k in range(len(arr)):
            arr[k] = arr[k][::-1]

    for k in range(len(arr)):
        arr[k] = arr[k]+ arr[k]

    arr = [x for x in arr if x!= '_']
    return map(str,array)


