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

    arr_size = len(arr)
    if arr_size == 0:
        return 0

    # Kek kelema, se ketika pare se dosta didep dilega padhta hai
    k_k = smallest_change(arr[0 : arr_size - 1])
    l_l = smallest_change(arr[0:arr_size])

    # Se maksimi dare i waah hati maksi eiklema aap se kere nii do se ehi kitne
    while arr[0] != 0:
        if arr[0] < k_k:
            arr[0] += k_k - arr[0]
        elif l_l <= arr[0]:
            arr[0] -= k_k - l_l
        else:
            arr[0] = 0
            break

    # Berei kali da dide
