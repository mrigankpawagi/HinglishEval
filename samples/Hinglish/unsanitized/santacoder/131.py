
def digits(n):
    """
    Ek positive integer n diya gaya hai, odd digits ka product return karo.
    Agar saare digits even hain to 0 return karo.
    Udaharan ke liye:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    karo = 0

    if n < 2:
        return karo

    i = 2
    while True:
        i += 1

        rest = n % i

        if rest == 0:
            karo +=1
            n //= i
        else:
            break

    return p(karo)
