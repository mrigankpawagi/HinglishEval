
def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    numerator = 0

    while N > 0:
        digit = N % 2
        if not digit:
            N = N / 2
        else:
            N = N / 2

        numerator = numerator * 10 + digit

    return str(numerator)


if __name__ == '__main__':
    print solve(1000)
    print solve(150)
    print solve(147)
