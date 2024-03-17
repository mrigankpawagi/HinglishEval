def starts_one_ends(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo 1 se start hote hain ya 1 pe end hote hain.
    """
    if n == 1:
        return 2
    else:
        return 2 * (10 ** (n - 1))
