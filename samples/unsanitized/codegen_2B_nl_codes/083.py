
def starts_one_ends(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo 1 se start hote hain ya 1 pe end hote hain.
    """
    if n == 0:
        return 0
    for i in range(2, n):
        if n % i is 0:
            return 0
    return 1


