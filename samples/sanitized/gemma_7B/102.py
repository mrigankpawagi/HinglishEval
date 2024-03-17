
def choose_num(x, y):
    """
    Yeh function do positive numbers x aur y leta hai aur return karta hai
    sabse bada even integer jo range [x, y] mein inclusive hai. Agar 
    aisa koi number nahi hai, toh function ko -1 return karna chahiye.

    Jaise ki:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x < 0 or y < 0:
        return -1
    if x > y:
        x, y = y, x
    if x % 2 == 0:
        return x
    else:
        for i in range(x + 1, y + 1):
            if i % 2 == 0:
                return i
        return -1

