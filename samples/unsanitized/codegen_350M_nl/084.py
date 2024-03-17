
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
    kato=0
     for i in range(1,N):
         # kato+=kato-#
         a=0
         for j in range(K): # a * a
             if N=j:
                 kato+=1
             else:
                 kato+=1
         kato+=a
     print(kato)
    print("Agar N = {}".format(kato))
    print("\n".join(f'{j+j:}' for j in kato))
    return(1+kato)


