
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

    # Base Cases:
    n = len(arr)
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return abs(arr[0] - arr[1])

    sorted_arr = sorted(arr)

    smallest_diff = abs(sorted_arr[0] - sorted_arr[1])
    for index in range(2, n):
        if abs(sorted_arr[index] - sorted_arr[index - 1]) < smallest_diff:
            smallest_diff = abs(sorted_arr[index] - sorted_arr[index - 1])

    return smallest_diff


# O(n*logn*2)
