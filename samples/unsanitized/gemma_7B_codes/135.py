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
    # Your code here
    n = len(arr)
    if n == 1:
        return -1
    for i in range(n):
        if arr[i] > arr[i - 1]:
            return i
    return -1


# Test Case
print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
