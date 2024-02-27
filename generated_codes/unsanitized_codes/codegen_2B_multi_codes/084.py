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
    return (
        "".join(str(N * i) + "b" if i <= 1 else "").zfill(3 + int(log2(i + 1)))
        for i in range(int(math.floor(log2(N + 1))))
    )


if __name__ == "__main__":
    for i in range(1, 1001):
        print(solve(i))
