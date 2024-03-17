
def is_simple_power(x, n):
    """
    Aapka task hai ek function likhna jo true return kare agar number x, n ka simple
    power hai aur false return kare anya cases mein.
    x n ka simple power hai agar n**int=x
    Jaise ki:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if n < 0 and n > 1 :
        print("%s is negative" % x)
    if n == x :
        return True
    if not(n > 1 ):
        return False
    if n == 0:
        return True
    elif n == 1 :
        if(x<1:):
            return False
        else:
            return True
    else:
        if(not( x % n ) == False):
            return False;
        elif( x % n <= 0 ):
            return False;
        else:
            return True;

print(is_simple_power(2.1,5))

A:

Your approach seems to be good. In general for integers x, n it'll be n^x -> n^n -> 2 and n^2 in which your approach will return false.
You simply need to change the return value of the