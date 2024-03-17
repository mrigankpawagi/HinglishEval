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
    # Check inputs to function
    if N <= 0:
        print("Invalid input!")
        return -1
    # 1. Calculate the sum of digits of N
    digitsSum = sum(map(int, str(N)))
    # 2. Convert the sum of digits of number N to binary
    binary = bin(digitsSum)
    return binary