
def solve(N):
    """
    Diye gaye positive integer N ka, uske digits ka total sum binary mein return karo.
    
    Udaharan
        Agar N = 1000 hai, to digits ka sum hoga 1 aur output honi chahiye "1".
        Agar N = 150 hai, to digits ka sum hoga 6 aur output honi chahiye "110".
        Agar N = 147 hai, to digits ka sum hoga 12 aur output honi chahiye "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         binary number ka ek string
    """
    def check(str):
        # check each digit to determine if sum
        for i in range(10):
            if int(str[i]) + int(str[i+1])+ int(str[i+2]) == 9999 and int(str[i])*int(str[i+1])*int(str[i+2])<=10:
                return False
        return True    
        
    total = str(HangmanProblem.total(N))
    
    if total == N:
        output = N
        return output
    
    if not check(total):
        return -1    
    print("Wrong!")
    return solve(N)
    
N = 1000
result = solve(N)
print(result)