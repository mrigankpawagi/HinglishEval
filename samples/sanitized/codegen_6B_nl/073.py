
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
    smallest_change = (0, 4)
    minimum_change = (-0, -0)
    for number_in_change, number_in_array in zip(arr, arr):
        if (abs(number_in_change - number_in_array) <= 1):
            minimum_change = smallest_change
            minimum_change[0] = number_in_change
            minimum_change[1] = number_in_array
            break
        else:
            smallest_change = (number_in_change - number_in_array, number_in_change - number_in_array)

    return smallest_change 
