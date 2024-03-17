
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
    
    res = 0
    while N:
        res = res*2 + (N%2)
        N = N//2
    return res
    

assert 22 == solve(22)
assert 3 == solve(3)
assert 4 == solve(4)
assert 7 == solve(7)
assert 17 == solve(17)
assert 12 == solve(12)
assert 100 == solve(100)
assert 0 == solve(1)
assert 0 == solve(0)
assert 4 == solve(15)
assert 13 == solve(151)
assert 1111 == solve(1000)
assert 110 == solve(150)
assert 110 == solve(145)
assert 1015 == solve(1545)
assert 11010111 == solve(10000)
assert 110 == solve(147)
assert 110 == solve(146)