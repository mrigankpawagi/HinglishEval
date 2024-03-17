
def digits(n):
    """
    Ek positive integer n diya gaya hai, odd digits ka product return karo.
    Agar saare digits even hain to 0 return karo.
    Udaharan ke liye:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 2:
        return 0
    s1 = re.search("^([\\d])+(.[\\d])*$", str(n), re.M)
    s2 = re.search("^([\\d])+(.[\\d])*$", str(n - 1), re.M)
    karo = s1.group(1) + s2.group(1)
    if karo[:1] == "0":
        return karo[1:]
    return karo[:-1]

