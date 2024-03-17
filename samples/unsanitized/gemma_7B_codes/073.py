
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
    # Write your code here
    n = len(arr)
    if n == 1:
        return 0
    if n == 2:
        return 1 if arr[0] != arr[1] else 0
    if n == 3:
        return 1 if arr[0] != arr[1] or arr[1] != arr[2] else 0
    if n == 4:
        return 2 if arr[0] != arr[1] or arr[1] != arr[2] or arr[2] != arr[3] else 0
    if n == 5:
        return 2 if arr[0] != arr[1] or arr[1] != arr[2] or arr[2] != arr[3] or arr[3] != arr[4] else 0
    if n == 6:
        return 3 if arr[0] != arr[1] or arr[1] != arr[2] or arr[2] != arr[3] or arr[3] != arr[4] or arr[4] != arr[5] else 0
    if n == 7:
        return 3 if arr[0] != arr[1] or arr[1] != arr[2] or arr[2] != arr[3] or arr[3] != arr[4] or arr[4] != arr[5] or arr[5] != arr[6] else 0
    if n == 8:
        return 4 if arr[0] != arr[1] or arr[1] != arr[2] or arr[2] != arr[3] or arr[3] != arr[4] or arr[4] != arr[5] or arr[5] != arr[6] or arr[6] != arr[7] else 0
    if n == 9:
        return 4 if arr[0] != arr[1] or arr[1] != arr[2] or arr[2] != arr[3] or arr[3] != arr[4] or arr[4] != arr[5] or arr[5] != arr[6] or arr[6] != arr[7] or arr[7] != arr[8