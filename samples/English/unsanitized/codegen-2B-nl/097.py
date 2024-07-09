
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    if (a < 0) or (b < 0):
        pass
    if a % 10 == 0 and b % 10 == 0:
        total = multiply(a/10, b/10)
    elif a % 10!= 0 or b % 10!= 0:
        total = 0
    return total


# Find the digit sum of the two numbers.
