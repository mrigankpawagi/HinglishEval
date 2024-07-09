
def starts_one_ends(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo 1 se start hote hain ya 1 pe end hote hain.
    """
    count = 0
    for i in range(1, n+1):
        if i == 1 or i % 10 == 1:
            count += 1
    return count

