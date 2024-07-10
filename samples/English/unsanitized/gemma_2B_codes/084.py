
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
    number = N
    sum_binary = ""
    while number > 1:
        sum_binary = str(N%2) + sum_binary
        N = N//2
    sum_binary =  str(N%10) + sum_binary
    total_binary = str(bin(sum_binary))
    return total_binary[2:]
    # a simple version of the problem :D

if __name__ == "__main__":
    a = input()
    b = solve(a)
    print(b)
