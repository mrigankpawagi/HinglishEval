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
    # If N = 500000, return "110".
    if int(N) <= 10000:
        N_repr = bin(N)
        result = N_repr[2:]
    # If N = 150000 return "1100".
    elif int(N) <= 150000:
        N_repr = bin(N)[2:]
        result = "".join(map(lambda x: "1" if N in x else "0", N_repr))
    # If N = 147000 return "1100".
    elif int(N) <= 147000:
        N_repr = bin(N)[2:]
        result = "".join(map(lambda x: "1" if N in x else "0", N_repr))
    else:
        raise ValueError("Oops... It is impossible to get this. Sorry.")
    return result