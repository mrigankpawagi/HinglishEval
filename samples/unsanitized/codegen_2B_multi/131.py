def digits(n):
    """
    Ek positive integer n diya gaya hai, odd digits ka product return karo.
    Agar saare digits even hain to 0 return karo.
    Udaharan ke liye:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n <= 0:
        return 0
    odd = 0
    even = n
    while even:
        s1 = even % 10
        s2 = s2 = 0
        while s1:
            s2 = (s1 * 10) + s2
            s1 = s1 / 10
        if s2 != 0:
            odd = 1
        even = even / len(str(s2))
        print(odd)
    return odd
