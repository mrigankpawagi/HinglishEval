
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

total_value=0
for n1 in range(2,10000):
    n=n1  # number of digits
    k,x=0,0
    (k,x)=starts_one_ends(n)
    v = x
    print k
    total_value+=v
    v = v * 10
    v+=x
    print v   
            
print total_value

# total_value=0
# for  n in range(2,10000):
#      v = x
#      (k,x)=starts_one_ends(10*n)
#      total_value+=v
#      v = v * 100
#      v+=x
#      print n
#      print v
    
# print total_value
