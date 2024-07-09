
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
    if isdigit(b):
        result = (b, 0)
        if isdigit(a):
            result = (b, 1)
    else:
        result = (b[-1], b * b[1:-1])
    return result
