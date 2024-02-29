
def starts_one_ends(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo 1 se start hote hain ya 1 pe end hote hain.
    """
    if n < 10:
        return []
    else:
        return [i for i in range(10, n + 1) if i % 10 == 1 or i % 10 == 9]
