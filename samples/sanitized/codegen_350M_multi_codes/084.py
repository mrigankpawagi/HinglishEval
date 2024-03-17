
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
    
    if type(N)!= type([]):
        raise ValueError('Expected List')
        
    if len(N) < 1:
        raise ValueError('Empty List')
        
    for i in range(1, len(N)):
        if type(N[i])!= type([]):
            raise ValueError('Expected List')
        if type(N[i][0])!= type(''):
            raise ValueError('Expected String')
    
    for i in range(1, len(N)):
        if type(N[i])!= type([]):
            raise ValueError('Expected List')
    
        bin = ''
        for item in N[1+i]:
            bin = str(bin + str(item))
        
    print(bin)
        
    for i in range(1, len(N)):
        if len(bin) == 1:
            break
        
        karoku = int(bin)
        
        if type(karoku)!= type([]):
            raise ValueError('Expected List')
        if len(karoku) < 1:
            raise ValueError('Empty List')
            
        for karoforza in range(0, 6):
            if type(karoku[i]) == type([]''''):
                karoforza = int(karor)
            elif type(karoku[i]) == type([]'0'):