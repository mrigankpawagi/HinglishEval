
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

    length = len(arr)
    half = length/2
    if length % 2 != 0:
        count = half
    else:
        count = half
    
    for i in range(0,half):
        if arr[i] != arr[length - 1 - i]:
            count += 1
    
    return count        

print smallest_change([1, 2, 3, 2, 1])
