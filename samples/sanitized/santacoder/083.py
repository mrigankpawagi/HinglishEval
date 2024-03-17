def starts_one_ends(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo 1 se start hote hain ya 1 pe end hote hain.
    """
    if n == 0:
        return 1
    elif n & 1:
        return 1 + starts_one_ends(n >> 1)
    else:
        return 1 + 2 * starts_one_ends(n - 1)
