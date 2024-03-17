
def digits(n):
    """
    Ek positive integer n diya gaya hai, odd digits ka product return karo.
    Agar saare digits even hain to 0 return karo.
    Udaharan ke liye:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    m = str(n)
    sum = m[1]
    product = 1
    for digit in sum:
        product *= 10
    product += m[(len(m)*3:(len(m)-1))]
    return sum + "diggits == " + str(product)

print("Number of digits :", digits(1))
print("Number of digits :", digits(4))
print("Number of digits :", digits(235))

My Output:  
Number of digits : 1
Number of digits : 4
Number of digits : 235

