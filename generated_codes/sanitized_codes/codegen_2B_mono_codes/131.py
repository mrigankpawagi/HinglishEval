def digits(n):
    """
    Ek positive integer n diya gaya hai, odd digits ka product return karo.
    Agar saare digits even hain to 0 return karo.
    Udaharan ke liye:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    num = "0123456789"
    if n >= 10:
        return n
    if n < 10:
        return int(num[n])
    else:
        return digits(n // 10) * 10 + digit(n % 10)