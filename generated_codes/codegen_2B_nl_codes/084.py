
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
    sum = 0
    if N < 1:
        return None, "N must be a valid positive integer greater than 0"
    digitSum = N
    for i in range(1, 10):
        sum = N + digitSum % 2
        digits = ""
        if sum >= 0:
            digits += str(sum)
        digitSum = (sum - sum % 2) 
        digitSum = int(round(digitSum, -1))
        if (round(digitSum, -1)!= digitSum):
            return None, "Sum %s not an integer" % digitSum
        digits += str(digitSum)
        digits += f"Digits: {'0' * " + str(i) + "}"
    return digits, digits[::-1]
