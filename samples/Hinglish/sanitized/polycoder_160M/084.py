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
    N = float([N] * len([N]))
    if N <= 0:
        return ""

    # N = 10^N
    result = "\x00"

    for i in range(N):
        result += "\xff" * N
        result += "\xff" * i

    return result + "\x00"
