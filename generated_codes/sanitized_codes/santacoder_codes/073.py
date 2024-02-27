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
    arr = [int(x) for x in arr]
    count = 0
    prev_min = float("inf")
    # i = 1 j = i+1 k= j+1
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            count += 1
            prev_min = min(prev_min, arr[i] - arr[i + 1], arr[j] - arr[j + 1])
    return count, prev_min
