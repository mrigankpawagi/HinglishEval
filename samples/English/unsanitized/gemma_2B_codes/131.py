
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    s = 1
    n = int(n)
    for i in range(2, n):
        if n % 2 == 0:
            s *= n
            n += 1
    #n = int(n**2)
    return s

if __name__ == '__main__':
    print(digits(23))
    print(digits(4))
