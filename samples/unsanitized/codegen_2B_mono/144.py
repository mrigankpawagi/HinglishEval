
def simplify(x, n):
    """
    Aapka task hai ek function implement karna jo expression
    x * n ko simplify karega. Yeh function True return karega agar x * n ka evaluation ek whole number hota hai aur False
    otherwise. Dono x aur n, fraction ka string representation hai, aur inka format aisa hota hai,
    <numerator>/<denominator> jahan dono numerator aur denominator positive whole numbers hote hain.

    Aap maan sakte hain ki x, aur n valid fractions hain, aur inka denominator zero nahi hota.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    if( x == "0"):
        return False
    n1 = n[::-1]
    a = x.split("/")
    b = n1.split("/")
    count = 0
    if a[1].strip() == "":
        return False
    for i in a:
        if i == "":
            continue
        if (int(b[count]) % int(i)!= 0):
            return False
        count += 1
    return count == len(n1)
        
    
    
    return False
    
    # code here
    pass


#{ 
#  Driver Code Starts

