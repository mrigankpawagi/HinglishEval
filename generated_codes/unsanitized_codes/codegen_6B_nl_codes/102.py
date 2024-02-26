
def choose_num(x, y):
    """
    Yeh function do positive numbers x aur y leta hai aur return karta hai
    sabse bada even integer jo range [x, y] mein inclusive hai. Agar 
    aisa koi number nahi hai, toh function ko -1 return karna chahiye.

    Jaise ki:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    a = x
    b = y
    if a % 2 == 0 and a > y:
        return a - y
    elif a % 2 == 0 and a < y:
        return a + y
    elif a % 2 == 0 and b % 2 == 1:
        return -1
    elif a % 2 == 0 and b % 2 == 0:
        return a
    elif a % 2 == 0:
        return x
    elif b % 2 == 0:
        return y
    elif a % 2 == 1:
        return x + y
    else:
        return -1

