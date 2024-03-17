def choose_num(x, y):
    """
    Yeh function do positive numbers x aur y leta hai aur return karta hai
    sabse bada even integer jo range [x, y] mein inclusive hai. Agar
    aisa koi number nahi hai, toh function ko -1 return karna chahiye.
    Jaise ki:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    choice = 10**19
    # print("x is", x, "y is", y)
    if x % 2 == 0:
        x //= 2
        choice = min(x * y, choice)
        # print("choice at", choice, "is")
    if y % 2 == 0:
        y //= 2
        choice = min(x * y, choice)
        # print("choice at", choice, "is")
    return choice if choice != 10**19 else -1