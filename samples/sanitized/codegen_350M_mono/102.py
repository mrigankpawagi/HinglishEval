def choose_num(x, y):
    """
    Yeh function do positive numbers x aur y leta hai aur return karta hai
    sabse bada even integer jo range [x, y] mein inclusive hai. Agar
    aisa koi number nahi hai, toh function ko -1 return karna chahiye.
    Jaise ki:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x % 2 == 0:
        if y % 2 == 0:
            if y != 0:
                return choose_num(x, y - 1)
            else:
                if x <= 1:
                    return -1
                if len(str((pow(x, y)))) > 10:
                    return 0
                else:
                    return -1
        else:
            if y != 0:
                return choose_num(x - 1, y)
            else:
                if x > 1:
                    return 0
                if len(str((pow(x, -2)))) > 10:
                    return 0
                else:
                    return -1
    else:
        if y % 2 == 0:
            if y != 0:
                return choose_num(x, y - 1)
            else:
                return choose_num(x + 1, y)
        else:
            if y != 0:
                return choose_num(x - 1, y - 1)
            else:
                return choose_num(x + 1, 0)