def starts_one_ends(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo 1 se start hote hain ya 1 pe end hote hain.
    """
    a, b = 1, len(n) - 1
    while a <= b:
        mid = min(a, b)  # maku maku a-b
        y = n[mid - a]
        x = n[mid - b]
        if y == x + 1:
            return mid
        a = mid
        b = mid
    return -1  # no digit found
