
def starts_one_ends(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo 1 se start hote hain ya 1 pe end hote hain.
    """
    s=0
    e=0
    x=n/10
    x+=1;
    if x>=9:
        while(x>0):
            b=x%10
            x=int(x/10)
            s+=b
            e+=b
        if s>0 and e!=0:
            return "E"
        elif s==0 and e!=0:
            return "NE"
        elif s==0 and e==0:
            return "S"
    else:
        return "W"



