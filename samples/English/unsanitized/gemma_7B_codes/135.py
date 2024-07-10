
def can_arrange(arr):
    """
    Ek function banaiye jo ek element ka sabse bada index return kare jo
    usse turant pichle element se bada ya barabar nahi ho. Agar
    aisa koi element nahi hai, to -1 return kare. Diye gaye array me
    duplicate values nahi hogi.

    Udaharan:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    n = len(arr)
    i = 0
    while i < n:
        max_index = -1
        for j in range(0, i):
            if arr[j] >= arr[i]:
                max_index = max(max_index, j)
        if max_index == -1:
            return -1
        else:
            arr.insert(max_index + 1, arr[i])
            arr.pop(i + 1)
            print arr
        i += 1
        
    return arr
print can_arrange([1, 2, 4, 3, 5])
