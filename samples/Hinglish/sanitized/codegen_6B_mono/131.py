def digits(n):
    """
    Ek positive integer n diya gaya hai, odd digits ka product return karo.
    Agar saare digits even hain to 0 return karo.
    Udaharan ke liye:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    result = 1
    for num in n:
        if num % 2 == 0:
            result *= num
        else:
            return 0
        return result