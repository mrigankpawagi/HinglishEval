def digits(n):
    """
    Ek positive integer n diya gaya hai, odd digits ka product return karo.
    Agar saare digits even hain to 0 return karo.
    Udaharan ke liye:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    total = sum([d for d in range(1, n + 1) if n % d == 0])
    if n:
        rem = n % 10
        return int(d[0] for d in digits(total - rem))
    return total