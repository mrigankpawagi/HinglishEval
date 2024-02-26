
def starts_one_ends(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo 1 se start hote hain ya 1 pe end hote hain.
    """
    return (((int(n/1000)) +1), ((int(n/100))%10 +1))
    
    
    
count = 1
while count>0:
    count = 0
    temp = (list(map(int,input().split())))
    length = len(temp)
    for i in range(length):
        
        for j in range(i,length):
            a = int("".join(str(temp[i:j+1])))
            if (a>9999):
                continue
            else:
                if (isPrime[a]==True):
                    temp = a
                    print ("%d/%d"%("".join(str(temp)), int(isPrime[a])))
                    count +=1
                    break
                    
       
    if (count==0):
        print ("0")
        
