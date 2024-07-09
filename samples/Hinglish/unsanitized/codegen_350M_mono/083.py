
def starts_one_ends(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo 1 se start hote hain ya 1 pe end hote hain.
    """
    if n < 2:
        return (2)
    return (starts_one_ends[n - 1] + 1) ** 2
