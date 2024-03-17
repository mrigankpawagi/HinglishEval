def digits(n):
    """
    Ek positive integer n diya gaya hai, odd digits ka product return karo.
    Agar saare digits even hain to 0 return karo.
    Udaharan ke liye:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    has_odd = False
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= int(digit)
            has_odd = True
    if has_odd:
        return product
    else:
        return 0
