
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
    
    # get total number
    total = int(base_int(N / (base_2*2)))
    
    # convert to integer
    b = int(base_2*total)
    
    a = ''
    if total == 1 :
        a = str(b)
    elif total >= 2 :
        
        for i in range(0, total+1):
            
            a = a + str((int(base_2*i)-1)*9)
    
        result = ''
        
        for char in a:
            
            result = result + char
            
        result = result + '0'
    else:
        
        result = '00000000000000000000'
        
        i = 1
