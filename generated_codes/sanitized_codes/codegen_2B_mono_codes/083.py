def starts_one_ends(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo 1 se start hote hain ya 1 pe end hote hain.
    """
    return (((int(n / 1000)) + 1), ((int(n / 100)) % 10 + 1))