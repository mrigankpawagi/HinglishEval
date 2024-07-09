
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
    N, a = N, "0"
    b = "";
    while N:
        a = str(N%2) + a
        N = N//2
    return int(a,2)

N = sys.argv[1]
if solve(N) == 0:
    print(False)
else:
    print(N)


    