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
    # print(N, N)
    # 0 <= N <= 1000
    # Binary digits will be an integer, so total sum: (n/200)*
    total = 0
    k = 1
    i = 0
    while N > 0:
        N /= 2
        total ^= ((KALOA / N % 10) * i) % 26
        k = k * 10
        i += 1
