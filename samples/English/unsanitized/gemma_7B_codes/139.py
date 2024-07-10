
def special_factorial(n):
    """
    Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    jaha n > 0

    Jaise ki:
    >>> special_factorial(4)
    288

    Ye function ek integer input ke roop me lega aur is integer ka special
    factorial return karega.
    """
#  @param n: the number whose special_factorial we want to calculate
    """
    Return brazilian factorial of n
    A brazilian factorial is factorial(n)* factorial(n-1)*...*factorial(1)
    
    INPUT: n (int >= 0)
    
    OUTPUT: brazilian factorial of n
    """

    return n*(n-1)%1000000007 if n>1 else 1

#  @param n: an integer
#  @return: the special factorial of n, which is factorial(n)* factorial(n-1)* ... * factorial(1)
