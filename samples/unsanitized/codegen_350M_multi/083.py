
def starts_one_ends(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo 1 se start hote hain ya 1 pe end hote hain.
    """
    if n <= 0:
        return
    if n == 1:
        return 1
    if n > 1:
        for i in range(n - 1):
            if is_starts_one_ends(i) == 1 and is_starts_one_ends(i + 1) == 1 and is_starts_one_ends(i + 2) == 1:
                return i + 2
            if is_starts_one_ends(i + 1) == 1 and is_starts_one_ends(i + 2) == 1 and is_starts_one_ends(i + 3) == 1:
                return i + 1
            if is_starts_one_ends(i + 1) == 1 and is_starts_one_ends(i + 2) == 1 and is_starts_one_ends(i + 3) == 1:
                return i + 2
