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
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[1] if arr[0] > arr[1] else arr[0]
    sabse_badaki = -float("inf")
    n = 2
    while n <= len(arr):
        mid = len(arr) // n
        while mid * n < len(arr):
            sabse_badaki = max(sabse_badaki, arr[mid * n - 1] - (mid - 1) * n)
            n += 1
        n += 1
    return max(sabse_badaki, 0)