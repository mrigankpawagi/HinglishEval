
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
    if N < 0 or N > 10000:
        return None
    if N < 1 and N!= 1:
       raise RuntimeError("input to solve was"
                           "less than 1!")
    b := 0
    for digit in str(N):
        b    += (b << 1) * int(digit)
    return b

    # if there is only 1 digit
    # return the binary number that is the sum of first number and the sum of second number.

