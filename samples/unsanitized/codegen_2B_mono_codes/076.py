
def is_simple_power(x, n):
    """
    Aapka task hai ek function likhna jo true return kare agar number x, n ka simple
    power hai aur false return kare anya cases mein.
    x n ka simple power hai agar n**int=x
    Jaise ki:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if x**n == x:
        return True
    else :
        return False

# Input number
number1 = int(input("Enter number 1 :"))
number2 = int(input("Enter number 2 :"))
# Find the gcd
print("The GCD of", number1, "and", number2,"is",
    find_greatest_common_divisor(number1, number2))
# Find LCM
number1=(number1*(find_greatest_common_divisor(number1, number2)))
print("The LCM of",
number1, "and", number2,"is",
    find_last_n_factor(number1,number2))





