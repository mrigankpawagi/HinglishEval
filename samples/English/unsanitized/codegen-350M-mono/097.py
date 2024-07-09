
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
    sum = 0
    # for i in range (len(a)):
    #     sum = sum + int(a[i]) * int(b[i])
    # return sum
    for i in a:
        sum = sum + i
    for j in b:
        sum = sum * 10
        sum = str(sum)
    return sum

if __name__ == "__main__":
    print(multiply("1234", "4567"))


