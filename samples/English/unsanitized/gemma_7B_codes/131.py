
def digits(n):
    """
    Ek positive integer n diya gaya hai, odd digits ka product return karo.
    Agar saare digits even hain to 0 return karo.
    Udaharan ke liye:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n == 0 or n == 1:
        return 1
    elif n % 10 == 0:
        return 0
    else:
        return n % 10 * digits(n // 10)


# Driver Code
if __name__ == '__main__':
    n = 10000
    ans = digits(n)
    print(f"Ans :: {ans}")
