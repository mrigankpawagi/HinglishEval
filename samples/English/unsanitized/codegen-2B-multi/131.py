
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    return (n&1) * ((n>>1)+1)
if __name__== '__main__':
    t = int ( input('Please input a positive number.\nNote: this program uses basic arithmetic on numbers, you can omit the parentheses around the number: eg. 123 \n>>> '))
    d = digits(t)
    print 'your answer is: %d' %(d)

