
def choose_num(x, y):
    """
    Yeh function do positive numbers x aur y leta hai aur return karta hai
    sabse bada even integer jo range [x, y] mein inclusive hai. Agar 
    aisa koi number nahi hai, toh function ko -1 return karna chahiye.

    Jaise ki:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    n = 10 ** 3 - x
    a1 = (y - n) / (x - n)
    if a1 == 0:
        return x
    d = (0 + 1) * a1
    s = d - (float(n) - d) / (float(a1) - d)
    if s == 0:
        return y
    i = int(s)
    if int(d) > 0:
        #
        # If positive a1 and negative a2 is negative s-1, 
        # return -1*y where y, (i-1) and (i+1) are negative and positive
        # respectively
        #
        if s < 0:   
            if d > 0:
                return -(i + 1 - i)
            elif d < 0:
                return -(i + 1 - i)
            else:
                return i
        #              
        else: