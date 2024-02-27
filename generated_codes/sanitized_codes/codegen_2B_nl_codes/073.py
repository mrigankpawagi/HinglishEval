
def smallest_change(arr):
    """
    Ek array arr diya gaya hai integers ka, usme se minimum kitne elements ko change karna padega 
    taaki array palindromic ban jaye. Ek palindromic array woh hota hai jo aage se bhi aur peeche se bhi 
    same padhta hai. Ek change me, aap ek element ko kisi bhi dusre element se replace kar sakte ho.

    Jaise ki:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """    
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 0

    i = 0
    minValue = 0
    smallestValue = len(arr) - 1

    while i < len(arr):
        if i % 2 == 0:
            if arr[i] < smallestValue:
                minValue = arr[i]
                smallestValue = i
        else:
            if arr[i] < minValue:
                minValue = arr[i]
                smallestValue = i

    return minValue
