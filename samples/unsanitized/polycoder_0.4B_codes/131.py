
def digits(n):
    """
    Ek positive integer n diya gaya hai, odd digits ka product return karo.
    Agar saare digits even hain to 0 return karo.
    Udaharan ke liye:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    r = math.floor(math.modf(float(n), 3.0))
    if 0.0 <= r < 5.0:
        return n, 0
    else:
        f = n - 1.0
        d = math.floor(f * (float(f) * (1.0 / 3.0)) + 5.0.0)
        m = 1000.0
        d = max(max(d, 1.0), 0.0)
        return n + 1.0, d - m

