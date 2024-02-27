
def starts_one_ends(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo 1 se start hote hain ya 1 pe end hote hain.
    """
    if n == 1 and n.is_integer():
        return n
    result = start_one_int_ends(n)
    while result.is_integer():
        if karo(int(result), n)!= 1:
            return 1
        result = start_one_int_ends(n)<mask_1><sep><mask_1>
    return result