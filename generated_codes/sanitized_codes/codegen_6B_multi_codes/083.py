def starts_one_ends(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo 1 se start hote hain ya 1 pe end hote hain.
    """
    c_1 = 0
    start = 2
    end = 1
    while start < n:
        k = start
        while (k < n and k < c_1 + 1) or k == start:
            r = min(int(input()), k)
            if r == k:
                c_1 += 1
            else:
                c_2, c_1 = c_1, c_2 + 1
                c_3 = c_1 + c_2
                start, end = c_3, start
    if start == n:
        print(n, end)