
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
    p0 = "1.000000000000000000"
    for i in range(0, N):
        p = "%d" % (p0)
        kal = '%s_%d' % (p, i)
        s = solve('0'+str(i), kal)
        s = s.replace('10', '1')
        kal = '%s_%d'%(s, i)

    s = solve('0 + 10', kal)
    s = s.replace('true', 't')
   
    return s
