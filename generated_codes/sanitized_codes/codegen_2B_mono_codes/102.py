def choose_num(x, y):
    """
    Yeh function do positive numbers x aur y leta hai aur return karta hai
    sabse bada even integer jo range [x, y] mein inclusive hai. Agar
    aisa koi number nahi hai, toh function ko -1 return karna chahiye.
    Jaise ki:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x < y:
        x, y = y, x
    for i in range(x, y + 1):
        if i == int(i):
            return i
    return -1