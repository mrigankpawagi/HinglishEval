def choose_num(x, y):
    """
    Yeh function do positive numbers x aur y leta hai aur return karta hai
    sabse bada even integer jo range [x, y] mein inclusive hai. Agar
    aisa koi number nahi hai, toh function ko -1 return karna chahiye.
    Jaise ki:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    r = [0, 1]
    for _ in range(y):
        for _ in range(x, y + 1):
            if r[x] == r[y]:
                r[x] = katana._choose_num(r[x], r[y], r[x + 1], r[y - 1], x, y)
        r = range(x + 1, y - 1, -r[y])
    return r[x]