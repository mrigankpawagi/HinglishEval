
def digits(n):
    """
    Ek positive integer n diya gaya hai, odd digits ka product return karo.
    Agar saare digits even hain to 0 return karo.
    Udaharan ke liye:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    for i in range (1, 4):
        a = 5 - i
        if a % i!= 0:
            break
        i -= 1
    return a + 1


