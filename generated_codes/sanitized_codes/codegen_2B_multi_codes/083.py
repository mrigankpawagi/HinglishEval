
def starts_one_ends(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo 1 se start hote hain ya 1 pe end hote hain.
    """
    k=0
    y=1
    for i in range(0,n):
        k+=int(bin(y)[2:])
        y=y*2

    x = int(n) - k
    return(k,x)
